import logging
import os

import aiohttp
import discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv

from rules_view import (
    GENERAL_RULES,
    build_department_view,
    build_persistent_department_views,
    build_reply,
)

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID = os.getenv("GUILD_ID")
ALERT_USER_ID = int(os.getenv("ALERT_USER_ID", "1441030741998702592"))
PRIDE_API_URL = os.getenv("PRIDE_API_URL", "").rstrip("/")
PRIDE_API_KEY = os.getenv("PRIDE_API_KEY", "")

logger = logging.getLogger(__name__)
_runtime_error_count = 0
_alert_sent = False

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)


async def send_pride_event(interaction: discord.Interaction, event_name: str):
    if not PRIDE_API_URL or not PRIDE_API_KEY or interaction.guild_id is None:
        return
    payload = {
        "guild_id": interaction.guild_id,
        "user_id": interaction.user.id,
        "source_bot": "wraith",
        "event": event_name,
        "event_id": f"wraith:{interaction.id}",
        "metadata": {"command": event_name},
    }
    try:
        timeout = aiohttp.ClientTimeout(total=3)
        async with aiohttp.ClientSession(timeout=timeout) as session:
            async with session.post(
                f"{PRIDE_API_URL}/event",
                json=payload,
                headers={"X-Pride-Key": PRIDE_API_KEY},
            ) as response:
                if response.status >= 400:
                    logger.warning("Pride API returned HTTP %s", response.status)
    except (aiohttp.ClientError, TimeoutError) as error:
        logger.warning("Could not report event to Pride: %s", error)


@bot.tree.command(name="general", description="Post the General Rules Components V2 panel.")
async def general(interaction: discord.Interaction):
    await interaction.response.send_message(
        view=build_reply("GENERAL RULES", GENERAL_RULES)
    )


@bot.tree.command(name="security-rules", description="Post the Security rules Components V2 panel.")
async def security_rules(interaction: discord.Interaction):
    await interaction.response.send_message(view=build_department_view("security"))


@bot.tree.command(name="research-rules", description="Post the Research rules Components V2 panel.")
async def research_rules(interaction: discord.Interaction):
    await interaction.response.send_message(view=build_department_view("research"))


@bot.tree.command(name="technical-rules", description="Post the Technical rules Components V2 panel.")
async def technical_rules(interaction: discord.Interaction):
    await interaction.response.send_message(view=build_department_view("technical"))


@bot.tree.command(name="janitor-rules", description="Post the Janitorial rules Components V2 panel.")
async def janitor_rules(interaction: discord.Interaction):
    await interaction.response.send_message(view=build_department_view("janitor"))


@bot.tree.command(name="medical-rules", description="Post the Medical rules Components V2 panel.")
async def medical_rules(interaction: discord.Interaction):
    await interaction.response.send_message(view=build_department_view("medical"))


@bot.event
async def setup_hook():
    # Re-register the department V2 views so existing rule panels remain
    # interactive after a Railway restart.
    for view in build_persistent_department_views():
        bot.add_view(view)

    if GUILD_ID:
        guild = discord.Object(id=int(GUILD_ID))
        bot.tree.copy_global_to(guild=guild)
        await bot.tree.sync(guild=guild)
    else:
        await bot.tree.sync()


@bot.event
async def on_app_command_completion(
    interaction: discord.Interaction, command: app_commands.Command
):
    await send_pride_event(interaction, f"command:{command.qualified_name}")
    if command.qualified_name in {"general", "security-rules", "research-rules", "technical-rules", "janitor-rules", "medical-rules"}:
        await send_pride_event(interaction, "rules_view")


async def report_runtime_error(error: Exception, context: str) -> None:
    global _runtime_error_count, _alert_sent
    _runtime_error_count += 1
    logger.exception(
        "Runtime error in %s (error %d)", context, _runtime_error_count, exc_info=error
    )

    if _runtime_error_count <= 5 or _alert_sent:
        return

    try:
        user = bot.get_user(ALERT_USER_ID) or await bot.fetch_user(ALERT_USER_ID)
        await user.send(
            f"<@{ALERT_USER_ID}> the General-Rules bot has encountered "
            f"{_runtime_error_count} runtime errors. Latest context: {context}."
        )
        _alert_sent = True
    except (discord.DiscordException, ValueError) as alert_error:
        logger.error("Could not send runtime-error alert: %r", alert_error)


@bot.tree.error
async def on_app_command_error(
    interaction: discord.Interaction, error: app_commands.AppCommandError
):
    await report_runtime_error(error, "slash command")
    message = "Something went wrong while running that command."
    if interaction.response.is_done():
        await interaction.followup.send(message, ephemeral=True)
    else:
        await interaction.response.send_message(message, ephemeral=True)


@bot.event
async def on_error(event_method: str, *args, **kwargs):
    error = discord.ClientException(f"Unhandled error in event: {event_method}")
    await report_runtime_error(error, event_method)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} - bot is online.")


if __name__ == "__main__":
    if not TOKEN:
        raise RuntimeError("DISCORD_TOKEN is not configured.")
    bot.run(TOKEN)
