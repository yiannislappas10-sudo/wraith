from __future__ import annotations

import discord
from discord import ui


# EZ-9 has its own visual identity: industrial warning amber, steel-grey
# dividers, concise field-manual language, and no Project Haven ornamentation.
EZ9_RULES = {
    "attire": {
        "label": "Technology & Attire",
        "value": "ez9_attire",
        "description": "Equipment, clothing, and tech limits",
        "title": "01 // TECHNOLOGY & ATTIRE",
        "body": """Technology is scarce within the Exclusion Zone. Character outfits, equipment, and accessories must reflect the setting’s limited technological capabilities. Keep your character believable within the world.

**I. No Overly Advanced Technology**
Excessively advanced technology is prohibited. This includes, but is not limited to:
• Advanced exo-arms and powered prosthetics.
• Highly futuristic armor and equipment.
• Technology that far exceeds the setting’s established capabilities.

Technology should be primitive, scarce, improvised, or otherwise appropriate to the lore.

**II. Dress for the Exclusion Zone**
Your character’s clothing, equipment, and accessories must make sense for life inside an Exclusion Zone. Consider the setting, available resources, and established lore when creating your outfit.

Avoid items that feel out of place or contradict the world’s atmosphere.

**III. No Hate Symbols or Prohibited Imagery**
Clothing, accessories, symbols, and other visible items promoting racism, Nazism, or other prohibited hateful ideologies are strictly forbidden.

Violations may result in a permanent ban. Do not use your character’s outfit as a way to display or promote such imagery.

**IV. Technology Limits — Important Clarification**
For simplicity, all technology must remain within the equivalent of very early exosuit technology at most. This reflects the scarcity of advanced equipment in the setting.

Do not assume that every type of advanced prosthetic, powered armor, or futuristic device is permitted just because it exists in real life or in science fiction. When uncertain, ask the Lore Team before using it.

**V. Future Amendments**
Additional rules or clarifications may be issued by the designated Lore Team member: <@939434613468712962>.

Follow future announcements and approved changes.

> When in doubt, prioritize the lore over appearance. Your character should look like they belong in the Exclusion Zone.""",
    },
    "community": {
        "label": "Community Rules",
        "value": "ez9_community",
        "description": "Conduct and community standards",
        "title": "02 // COMMUNITY RULES",
        "body": """Welcome to our community! We maintain stricter standards than many other communities to prevent unnecessary conflicts and keep the environment comfortable as we continue developing.

**I. Keep Drama Out**
Do not bring personal drama, arguments, or ongoing conflicts into voice chats, General, or other community channels.
• First offense: 24-hour mute.
• Continued behavior after the mute: Kick, with an appeal available.
• Repeated offenses after that: Permanent ban without appeal.

**II. No Discrimination or Hate**
Racism, homophobia, sexism, or discrimination targeting someone’s race, gender, or identity is strictly prohibited.

This is a ban-worthy offense. Appeals may be considered at staff discretion, but you must provide credible evidence if claiming the behavior was accidental or unintentional. An appeal does not guarantee an unban.

**III. No Highly Sensitive Content**
Do not post or initiate discussions involving suicide, self-harm, NSFW content, or excessive graphic gore. Keep the community appropriate and comfortable for its members.

**IV. Use the Correct Channels**
Keep messages, discussions, and content in their designated channels. Follow channel descriptions and staff instructions.

**V. Respect Personal Boundaries**
Respect other members’ stated boundaries, both in and out of roleplay. Do not pressure people into interactions they have declined.

Set clear, reasonable boundaries and communicate changes respectfully. Boundaries should not be used to bypass established rules—for example, declaring your character immune to being killed in situations where death is permitted under the RP rules.

**VI. No Spamming**
Do not flood channels with repeated messages, excessive mentions, or other disruptive spam.

**VII. Keep Swearing to a Minimum**
Avoid excessive profanity. Please keep conversations reasonably comfortable and respectful for everyone.

**VIII. No Political Discussions**
Political debates, arguments about governments, and political jabs are not permitted. This rule applies regardless of political side. Keep political disputes out of the community to prevent unnecessary conflict.

> Staff may take action based on the severity and context of an incident. Follow these rules to help keep the community welcoming and focused on its intended purpose.""",
    },
    "roleplay": {
        "label": "Roleplay Rules",
        "value": "ez9_roleplay",
        "description": "IC conduct, combat, factions, and lore",
        "title": "03 // ROLEPLAY RULES",
        "body": """Standards established by the Lore Team to ensure an enjoyable, comfortable, and story-driven roleplay experience for everyone.

**I. Community Standards**
All standard community rules apply to roleplay. Being in character does not exempt you from following the server’s general rules.

**II. Sensitive Topics**
Suicide, self-harm, NSFW content, and other sensitive topics are prohibited in roleplay. Keep the experience appropriate and comfortable for all members.

**III. Combat & No Man’s Land**
Lethal combat and killing are only permitted in No Man’s Land. Outside of No Man’s Land, combat must remain non-fatal, such as shooting a character’s limbs or using non-lethal physical attacks. Do not kill characters outside the designated area.

**IV. Faction Relations & Lore**
This is a heavily story-driven roleplay environment. Before choosing or interacting with a faction, check its relations with other factions. Your character’s actions should respect the established lore and faction dynamics.

**V. Character Age**
All original characters (OCs) must be 18 years old or older. Minor characters are not permitted in this wasteland setting.

**VI. Character Limits & Lore Death**
You may have only one active character at a time. If your character is lore-killed or becomes permanently unplayable due to an approved story event, you may create a replacement character.

**VII. Faction Membership**
Each character may officially belong to only one faction. You may remain neutral, maintain friendships, or have rivalries with members of other factions. However, you may only join one faction once you have earned sufficient reputation.

**VIII. No Invincibility**
No invincibility, godmodding, or making your character immune to damage and consequences. Characters must remain vulnerable, and combat outcomes must be fair.

**IX. No Metagaming**
Do not use information your character has not learned in roleplay. Information obtained out of character (OOC) must not be used to gain an unfair in-character (IC) advantage.

**X. Faction Checks Before Combat**
Before opening fire on another character, check their faction using a PDA scanner when this feature becomes available. This is a recommended future feature and is not yet an active requirement.

---

## LORE TEAM NOTICE

Please do not use faction or infected role tags unless they have been assigned to you by the Lore Team or the Owner.

**NOMAD is the only permitted tag otherwise.**

Thank you for respecting the rules and helping us maintain an immersive roleplay environment.

— The Lore Team""",
    },
}


AMBER = 0xD98B22
STEEL = 0x242A31


def _rule_detail(key: str) -> ui.LayoutView:
    rule = EZ9_RULES[key]
    view = ui.LayoutView()
    panel = ui.Container(accent_color=AMBER)
    panel.add_item(ui.TextDisplay(f"# {rule['title']}"))
    panel.add_item(ui.TextDisplay("-# EZ-9 / FIELD MANUAL / AUTHORIZED COMMUNITY DIRECTIVES"))
    panel.add_item(ui.Separator())
    panel.add_item(ui.TextDisplay(rule["body"]))
    panel.add_item(ui.Separator())
    panel.add_item(ui.TextDisplay("-# Read the complete section. Lore and community standards apply together."))
    view.add_item(panel)
    return view


class EZ9RuleSelect(ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(
                label=item["label"],
                value=item["value"],
                description=item["description"],
                emoji=emoji,
            )
            for item, emoji in zip(
                EZ9_RULES.values(),
                ["⚙️", "▣", "⌖"],
            )
        ]
        super().__init__(
            placeholder="OPEN A DIRECTIVE  ▾",
            min_values=1,
            max_values=1,
            options=options,
            custom_id="wraith:ez9:rules:select",
        )

    async def callback(self, interaction: discord.Interaction):
        selected = self.values[0]
        key = next(
            (key for key, rule in EZ9_RULES.items() if rule["value"] == selected),
            None,
        )
        if key is None:
            await interaction.response.send_message(
                "Directive unavailable. Please try again.", ephemeral=True
            )
            return
        await interaction.response.send_message(view=_rule_detail(key), ephemeral=True)


class EZ9RulesView(ui.LayoutView):
    def __init__(self):
        super().__init__(timeout=None)
        panel = ui.Container(accent_color=AMBER)
        panel.add_item(ui.TextDisplay("# EZ-9  /  FIELD DIRECTIVES"))
        panel.add_item(
            ui.TextDisplay(
                "-# EXCLUSION ZONE OPERATIONS   •   RULES INDEX 01–03\n"
                "Three directives govern equipment, community conduct, and roleplay. "
                "Select a file below to open its full text privately."
            )
        )
        panel.add_item(ui.Separator())
        panel.add_item(
            ui.TextDisplay(
                "▰ **01  EQUIPMENT & ATTIRE**\n"
                "Technology limits, setting consistency, prohibited imagery.\n\n"
                "▰ **02  COMMUNITY CONDUCT**\n"
                "Respect, boundaries, sensitive content, and moderation.\n\n"
                "▰ **03  ROLEPLAY PROTOCOL**\n"
                "Combat zones, factions, character limits, and lore."
            )
        )
        panel.add_item(ui.Separator())
        panel.add_item(ui.ActionRow(EZ9RuleSelect()))
        panel.add_item(
            ui.TextDisplay(
                "-# EZ-9 // COMPLIANCE NOTICE: Staff may act on severity and context. "
                "Lore Team clarifications take precedence for setting-specific questions."
            )
        )
        self.add_item(panel)


def build_ez9_view() -> ui.LayoutView:
    return EZ9RulesView()
