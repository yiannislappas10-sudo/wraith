from __future__ import annotations

import discord
from discord import ui


SUPPORT_URL = "https://discord.gg/kCz3W4VT4"
COMMUNITY_GUIDELINES_URL = "https://discord.com/guidelines"


# ---------------------------------------------------------------------------
# General rules are intentionally left as-is. The five department rules below
# use the full Components V2 / dropdown presentation from the Security-Rules
# layout while remaining native to the Wraith Python bot.
# ---------------------------------------------------------------------------

GENERAL_RULES = """꧁ 𓆩✰༺☾ GENERAL RULES ☽༻✰𓆪꧂

**I. Explicit & Graphic Content**
Points won't be removed even if you're unbanned. To comply with Discord's Community Guidelines, explicit or graphic content is strictly prohibited.
• Pornographic or sexually explicit media → Permanent Ban
• Sexual roleplay, erotic discussions, or explicit requests → Warning / Mute
• Suggestive images, cropped NSFW, or filter bypasses → Indefinite Ban
• Graphic gore, mutilation, or real-life violent content → Permanent & Non-Appealable Ban
• Content depicting abuse, torture, or cruelty → Permanent & Non-Appealable Ban

**II. Respect & Conduct**
Treat every member with respect regardless of disagreements.
• Harassing, bullying, or targeting members → Temporary to Indefinite Ban
• Discrimination, hate speech, or offensive remarks → Permanent & Non-Appealable Ban
• Threatening violence, self-harm, or credible threats → Permanent Ban
• Sexual harassment, predatory behavior, or unwanted advances → Permanent & Non-Appealable Ban
• Sharing private information (Doxxing) → Permanent & Non-Appealable Ban

**III. Spam & Disruptive Behavior**
Keep conversations readable and avoid intentionally disrupting the community.
• Spam, excessive emojis, repeated messages, or keyboard smashing → Warning
• Mass mentions (@everyone / @here) without permission → Warning / Temporary Mute
• Advertising servers, communities, or products → Temporary Ban
• Using alternate accounts to avoid punishments (Alt Evasion) → Permanent Ban (All Accounts)
• Intentionally disrupting chats, events, or roleplay → Warning / Mute / Ban

**IV. Exploits & Security**
Any attempt to abuse Discord or the community will be taken seriously.
• Malware, phishing links, token grabbers, or malicious software → Permanent & Non-Appealable Ban
• Scamming, impersonating, or deceiving for gain → Permanent Ban
• Exploiting bots, loopholes, or server vulnerabilities → Admin Discretion

**V. Appropriate Content**
Please keep discussions suitable for the community.
• Political or religious debates intended to provoke arguments → Warning
• Deliberately offensive or inflammatory content → Warning / Temporary Ban
• Impersonating staff members or trusted individuals → Indefinite Ban
• Posting misleading information while pretending it is official → Warning / Ban

**VI. Staff Decisions**
Our staff team is responsible for maintaining a fair and enjoyable community.
• Staff decisions should be respected at all times.
• If you disagree with a punishment, use the proper appeal process instead of arguing publicly.
• Attempting to evade punishments will result in harsher penalties.
• Staff reserve the right to act on harmful behavior not explicitly listed.

**VII. Links & Advertising**
Unsolicited or unwanted links are not allowed anywhere in the server.
• Sending unwanted/unsolicited links (invite links, spam links, redirect links, etc.) → Warning / Mute
• Repeated link spam after a warning → Temporary to Permanent Ban
• Malicious or disguised links (see Exploits & Security) → Permanent & Non-Appealable Ban

**VIII. Character & Content Ownership**
Respect what other members have created.
• Drawing, writing, animating, or otherwise using someone else's OC/character requires their permission first → Warning
• Claiming or "reskinning" another member's character concept without permission → Warning / Ban
• Always credit the original creator when referencing someone else's lore or OC → Warning

**IX. Anti-Drama**
Keep conflicts out of public spaces.
• Personal conflicts, callouts, or disputes must be taken to DMs or a support ticket, not aired in public channels → Warning
• Stirring drama or baiting others into public arguments → Warning / Temporary Mute"""

SECURITY_RULES = [
    {
        "label": "1. Weapon Discipline",
        "value": "security_1",
        "description": "No firing without a valid threat, no mag-dumping",
        "title": "1. WEAPON DISCIPLINE",
        "bullets": [
            "Do not fire without a valid threat.",
            "No unnecessary firing or mag-dumping.",
            "Do not shoot personnel because of suspicion alone.",
            "Do not fire into crowds or populated areas recklessly.",
            "Keep your weapon under control at all times.",
        ],
    },
    {
        "label": "2. Identification",
        "value": "security_2",
        "description": "Verify who you're dealing with before acting",
        "title": "2. IDENTIFICATION",
        "bullets": [
            "Know who you are dealing with before taking action.",
            "Do not attack someone simply because they are unfamiliar.",
            "Ask questions and verify their authorization when appropriate.",
            "If you are unsure, get a superior rather than immediately escalating.",
        ],
    },
    {
        "label": "3. Post Discipline",
        "value": "security_3",
        "description": "Stay at your position, remain attentive",
        "title": "3. POST DISCIPLINE",
        "bullets": [
            "Stay at your assigned position unless given permission to leave.",
            "Do not abandon your post during minor incidents.",
            "Do not wander around the facility looking for trouble.",
            "Remain attentive while stationed.",
        ],
    },
    {
        "label": "4. Authority",
        "value": "security_4",
        "description": "Follow superiors, never abuse your rank",
        "title": "4. AUTHORITY",
        "bullets": [
            "Follow orders from authorized superiors.",
            "Do not give orders beyond your rank.",
            "Do not threaten or intimidate personnel because you have a weapon.",
            "Security authority must never be used for personal arguments.",
        ],
    },
    {
        "label": "5. Restricted Areas",
        "value": "security_5",
        "description": "No unauthorized access to restricted zones",
        "title": "5. RESTRICTED AREAS",
        "bullets": [
            "Do not allow unauthorized personnel into restricted areas.",
            "Do not enter restricted zones without proper authorization.",
            "Do not give other players access to areas they are not cleared for.",
        ],
    },
    {
        "label": "6. Incidents",
        "value": "security_6",
        "description": "Stay calm, protect personnel, report up",
        "title": "6. INCIDENTS",
        "bullets": [
            "Stay calm during emergencies.",
            "Protect nearby personnel and secure the area.",
            "Do not make an incident worse through reckless behavior.",
            "Report serious incidents to the appropriate superior.",
        ],
    },
    {
        "label": "7. Professional Conduct",
        "value": "security_7",
        "description": "No harassment, no starting conflicts on duty",
        "title": "7. PROFESSIONAL CONDUCT",
        "bullets": [
            "No harassment, bullying, or unnecessary aggression.",
            "Do not randomly detain or attack people.",
            "Do not start conflicts while on duty.",
            "Remain professional even when other personnel are being difficult.",
        ],
    },
    {
        "label": "8. Roleplay Discipline",
        "value": "security_8",
        "description": "No OOC info IC, no random kills",
        "title": "8. ROLEPLAY DISCIPLINE",
        "bullets": [
            "Do not use OOC information for IC decisions.",
            "Do not randomly kill players for entertainment.",
            "Follow the facility's RP rules.",
            "Keep your actions appropriate to your character's position.",
        ],
    },
    {
        "label": "9. Equipment",
        "value": "security_9",
        "description": "Don't misuse or take others' equipment",
        "title": "9. EQUIPMENT",
        "bullets": [
            "Do not misuse security equipment.",
            "Do not take another officer's equipment without permission.",
            "Report missing or damaged equipment to a superior.",
        ],
    },
    {
        "label": "10. Accountability",
        "value": "security_10",
        "description": "Report mistakes, repeated violations = discipline",
        "title": "10. ACCOUNTABILITY",
        "bullets": [
            "Mistakes must be reported instead of hidden.",
            "Repeated violations will result in disciplinary action.",
            "Severe misconduct may result in immediate suspension or removal from Security.",
        ],
    },
]

RESEARCH_RULES = [
    {
        "label": "1. Don't Harm Anyone",
        "value": "research_1",
        "description": "No harm to anyone in or out this division",
        "title": "1. DON'T HARM ANYONE",
        "bullets": ["Don't harm anyone in or out this division."],
    },
    {
        "label": "2. Stay In Your Lane",
        "value": "research_2",
        "description": "Do your business as a researcher",
        "title": "2. STAY IN YOUR LANE",
        "bullets": [
            "Do your business as a researcher (regardless of high or low rank).",
            "Each rank is provided their own place and business.",
        ],
    },
    {
        "label": "3. No Harm During Roleplay",
        "value": "research_3",
        "description": "No murder, assault, or guilt-tripping",
        "title": "3. NO HARM DURING ROLEPLAY",
        "bullets": [
            "During roleplay, do NOT murder, harm, assault, make uncomfortable, or guilt trip anyone.",
            "You're a researcher — not another division with their own tasks and goals.",
            "Our goal is to find artifacts and discover each specimen.",
        ],
    },
    {
        "label": "4. Be Humble & Kind",
        "value": "research_4",
        "description": "Avoid assaults and harmful things",
        "title": "4. BE HUMBLE & KIND",
        "bullets": [
            "Be humble and kind to others, avoid assaults and harmful things.",
            "Do not pick violence against other division personnel.",
        ],
    },
    {
        "label": "5. Pinning Messages",
        "value": "research_5",
        "description": "Only High Curator pins important messages",
        "title": "5. PINNING MESSAGES",
        "bullets": [
            "Only the High Curator pins messages that are important and need to be seen by other high-ups, including this division (Research Division).",
        ],
    },
    {
        "label": "6. Care For One Another",
        "value": "research_6",
        "description": "High or low rank, be careful with each other",
        "title": "6. CARE FOR ONE ANOTHER",
        "bullets": [
            "Care for one another, high or low rank, in each division.",
            "Do not harm or be rude to them — be cautious about what you've done.",
            "Hesitate before doing something next — think about whether it's right or wrong.",
        ],
    },
    {
        "label": "7. Evidence Is Kept",
        "value": "research_7",
        "description": "Records of assaults will be used against you",
        "title": "7. EVIDENCE IS KEPT",
        "bullets": [
            "There are records that will be used to hold you accountable for any assaults you've committed.",
        ],
    },
    {
        "label": "8. You're Being Watched",
        "value": "research_8",
        "description": "High-ups watch this division's actions",
        "title": "8. YOU'RE BEING WATCHED",
        "bullets": [
            "Not only the High Curator is watching — other higher-ups watch this division's actions toward one another too.",
        ],
    },
    {
        "label": "9. Suspension for Harm",
        "value": "research_9",
        "description": "Assault = suspension or imprisonment",
        "title": "9. SUSPENSION FOR HARM",
        "bullets": [
            "Suspension and imprisonment are given directly if you have assaulted or harmed any personnel.",
            "Begging for mercy will not help.",
        ],
    },
    {
        "label": "10. No Fake Friendliness",
        "value": "research_10",
        "description": "No assumptions, no rank flexing",
        "title": "10. NO FAKE FRIENDLINESS",
        "bullets": [
            "No assumptions, no showing fake friendliness toward others, no using rank as leverage over your name.",
            "Direct mute or suspension with no hesitation.",
        ],
    },
    {
        "label": "11. Don't Annoy High-Ups",
        "value": "research_11",
        "description": "Leave the High Curator and higher-ups alone",
        "title": "11. DON'T ANNOY HIGH-UPS",
        "bullets": [
            "Don't even think about annoying the High Curator or other high-ups while they're minding their own business.",
            "They will mark you for suspension.",
        ],
    },
]

TECHNICAL_RULES = [
    {
        "label": "1. No Blaming or Framing",
        "value": "technical_1",
        "description": "Don't act badly towards others",
        "title": "1. NO BLAMING OR FRAMING",
        "bullets": ["No one will act badly towards others, especially blaming people or framing them."],
    },
    {
        "label": "2. Act Responsibly",
        "value": "technical_2",
        "description": "Handle problems accordingly",
        "title": "2. ACT RESPONSIBLY",
        "bullets": ["If you encounter a problem, act accordingly and responsibly."],
    },
    {
        "label": "3. Reach Out If You're Hurting",
        "value": "technical_3",
        "description": "You can come to me or others",
        "title": "3. REACH OUT IF YOU'RE HURTING",
        "bullets": [
            "If you feel hurt or sad and someone is being mean to you, don't worry — you may reach out to me or others.",
        ],
    },
    {
        "label": "4. No Attacking or Harassing",
        "value": "technical_4",
        "description": "No insults or harassment",
        "title": "4. NO ATTACKING OR HARASSING",
        "bullets": [
            "No attacking people, and no insulting or harassing them.",
            "Serious consequences follow for anyone who does.",
        ],
    },
    {
        "label": "5. Represent The Division Well",
        "value": "technical_5",
        "description": "Don't embarrass the Technical name",
        "title": "5. REPRESENT THE DIVISION WELL",
        "bullets": ["No acting like a kid — do not embarrass our Technical name, or me."],
    },
    {
        "label": "6. Stay Serious In-Game",
        "value": "technical_6",
        "description": "OOC is fine with trusted people, in moderation",
        "title": "6. STAY SERIOUS IN-GAME",
        "bullets": [
            "Act serious in-game. You can be OOC with people you know, and have some fun — just don't take it too far.",
        ],
    },
    {
        "label": "7. Don't Ask For Special Permission",
        "value": "technical_7",
        "description": "It gets escalated to the higher-ups",
        "title": "7. DON'T ASK FOR SPECIAL PERMISSION",
        "bullets": [
            "Do not ask for special permission. If you do, I will gladly take this to the higher-ups.",
        ],
    },
    {
        "label": "8. Respect The Higher-Ups",
        "value": "technical_8",
        "description": "DM only for important matters",
        "title": "8. RESPECT THE HIGHER-UPS",
        "bullets": [
            "Do not mess with the higher-ups. If you have a problem, DM me — but only for important matters.",
        ],
    },
    {
        "label": "9. No Metagaming / Meta-Grudging",
        "value": "technical_9",
        "description": "Learn proper roleplay etiquette",
        "title": "9. NO METAGAMING / META-GRUDGING",
        "bullets": ["Don't metagame or meta-grudge. Learn the proper rules on how to roleplay."],
    },
]

JANITOR_RULES = [
    {
        "label": "1. Only 2 Chances",
        "value": "janitor_1",
        "description": "Break them all = suspension",
        "title": "1. ONLY 2 CHANCES",
        "bullets": [
            "You are required to follow the rules strictly — you only get 2 chances if you break them.",
            "If you break all of them, you will be suspended.",
        ],
    },
    {
        "label": "2. No Murder / Assault",
        "value": "janitor_2",
        "description": "No playing the victim either",
        "title": "2. NO MURDER / ASSAULT",
        "bullets": [
            "Don't even think about murdering or assaulting anyone to cause harm, or playing the victim.",
            "Doing so puts you at high risk of suspension.",
        ],
    },
    {
        "label": "3. Evidence Is Kept",
        "value": "janitor_3",
        "description": "Higher-ups can prove you guilty",
        "title": "3. EVIDENCE IS KEPT",
        "bullets": [
            "The higher-ups have records and evidence coming from you (low or high rank) to prove you guilty of any charges.",
        ],
    },
    {
        "label": "4. Don't Start Fights",
        "value": "janitor_4",
        "description": "Being a janitor doesn't excuse it",
        "title": "4. DON'T START FIGHTS",
        "bullets": [
            "Yes, janitors can be dangerous — that doesn't mean you can act like one just to harm others.",
            "Don't assume you can pick a fight on them — if someone sees you fighting with other personnel, both of you will be reported directly.",
        ],
    },
    {
        "label": "5. Act Your Age",
        "value": "janitor_5",
        "description": "Choose peace and humility",
        "title": "5. ACT YOUR AGE",
        "bullets": [
            "Choose peace and humility instead. Don't act like a kid in front of every player when your character is 18+ and should act like it.",
        ],
    },
    {
        "label": "6. No Annoying Other Divisions",
        "value": "janitor_6",
        "description": "Higher-ups are watching the evidence",
        "title": "6. NO ANNOYING OTHER DIVISIONS",
        "bullets": [
            "Don't choose annoyance or anything else against other division personnel.",
            "The higher-ups are reading your messages and can see the evidence of what, where, and when it happened.",
        ],
    },
    {
        "label": "7. No Fights, No Violence",
        "value": "janitor_7",
        "description": "Limit reports and disturbances",
        "title": "7. NO FIGHTS, NO VIOLENCE",
        "bullets": [
            "NO picking fights, NO violence, NO harming or annoying other personnel in or out of the division.",
            "NO giving unexpected reports until the limit is already 10+.",
            "NO disturbing the higher-ups unless it's actually important.",
        ],
    },
    {
        "label": "8. Higher-Ups Can Reach Out",
        "value": "janitor_8",
        "description": "If something looks wrong",
        "title": "8. HIGHER-UPS CAN REACH OUT",
        "bullets": [
            "The higher-ups can read or directly message the division at any time if they see you doing something that isn't clearly right.",
        ],
    },
    {
        "label": "9. The Limit Is 2 — No Exceptions",
        "value": "janitor_9",
        "description": "No assumptions, no changes",
        "title": "9. THE LIMIT IS 2 — NO EXCEPTIONS",
        "bullets": [
            "You only get 2 chances. No assumptions, no changing that number.",
            "If you broke them, there's no sympathy for the path you chose.",
        ],
    },
    {
        "label": "10. Mind Your Own Business",
        "value": "janitor_10",
        "description": "Follow the goals you were given",
        "title": "10. MIND YOUR OWN BUSINESS",
        "bullets": [
            "All personnel in this division must strictly mind their own business and follow the goals they were given.",
            "No violence-driven goals, ever.",
        ],
    },
    {
        "label": "11. Report, Don't Engage",
        "value": "janitor_11",
        "description": "Report to the head janitor",
        "title": "11. REPORT, DON'T ENGAGE",
        "bullets": [
            "Resume your own business — do not engage in a fight for someone else's sake.",
            "Report directly to the Head Janitor instead.",
        ],
    },
]

MEDICAL_RULES = [
    {
        "label": "01. Don't Make Enemies Out Of Lies",
        "value": "medical_1",
        "description": "No fabricating stories or false accusations",
        "title": "01. DON'T MAKE ENEMIES OUT OF LIES",
        "bullets": [
            "Do not fabricate stories, frame people, spread false accusations, or deliberately make someone look guilty for something they didn't do.",
            "This applies to everyone, including higher-ranking members.",
            "Rank does not make someone immune to accusations, and it does not make false ones acceptable.",
        ],
    },
    {
        "label": "02. Let People Choose For Themselves",
        "value": "medical_2",
        "description": "No guilt-tripping or pressuring anyone",
        "title": "02. LET PEOPLE CHOOSE FOR THEMSELVES",
        "bullets": [
            "Nobody should be pushed into doing something through guilt, pressure, emotional manipulation, threats, or persistence.",
            "A choice is only a choice when someone is actually free to say no.",
            "Boundary crossing will not be tolerated under my control.",
        ],
    },
    {
        "label": "03. Respect Goes Both Ways",
        "value": "medical_3",
        "description": "Respect and Reciprocity",
        "title": "03. RESPECT GOES BOTH WAYS",
        "bullets": [
            "Don't deliberately hurt, insult, humiliate, attack, or mistreat other members.",
            "We operate on Respect and Reciprocity: give others the same consideration you expect from them.",
        ],
    },
    {
        "label": "04. Don't Decide Relationships For Others",
        "value": "medical_4",
        "description": "Shipping needs everyone's consent",
        "title": "04. DON'T DECIDE RELATIONSHIPS FOR OTHER PEOPLE",
        "bullets": [
            "Shipping is fine when everyone involved is comfortable with it.",
            "Do not assign people relationships, pairings, romances, or similar dynamics without their permission.",
            "A refusal is enough — if someone becomes uncomfortable, drop the subject quickly.",
        ],
    },
    {
        "label": "05. Know Where The Joke Ends",
        "value": "medical_5",
        "description": "Stop when someone asks you to stop",
        "title": "05. KNOW WHERE THE JOKE ENDS",
        "bullets": [
            "Being playful, sarcastic, or annoying your friends is fine when everyone involved is enjoying it.",
            "Do not use anything as an excuse to keep going after someone has asked you to stop.",
            "Be someone people can actually work with.",
        ],
    },
    {
        "label": "06. Keep Violence Within Its Boundaries",
        "value": "medical_6",
        "description": "In-character violence needs a real reason",
        "title": "06. KEEP VIOLENCE WITHIN ITS BOUNDARIES",
        "bullets": [
            "Do not attack or injure someone without a legitimate reason, especially during roleplay.",
            "In-character violence should have a reason and be appropriate to the situation.",
            "Do not use force simply because you can — when authorization is required, get it.",
        ],
    },
]

RULESETS = {
    "security": SECURITY_RULES,
    "research": RESEARCH_RULES,
    "technical": TECHNICAL_RULES,
    "janitor": JANITOR_RULES,
    "medical": MEDICAL_RULES,
}

TITLES = {
    "security": "SITE AEGIS 17 — SECURITY RULES",
    "research": "RESEARCH DIVISION — RULES",
    "technical": "TECHNICAL DIVISION — RULES",
    "janitor": "JANITORIAL DIVISION — RULES",
    "medical": "MEDICAL DIVISION — RULES",
}

CLOSING_TEXT = {
    "security": (
        "*Security is a position of trust. If you cannot control your weapon, your authority, "
        "or your behavior, you will not remain Security.*\n\n"
        "**FAILURE TO FOLLOW THESE RULES WILL RESULT IN DISCIPLINARY ACTION**, including warning, "
        "suspension, demotion, or removal from Security depending on the severity of the violation."
    ),
    "research": (
        "*If you break these rules — any or all of them — I will directly kick you out of this "
        "server, or worse, fire you with no mercy. I don't care if you feel sorry for anyone who "
        "gets kicked or fired — it's their own fault for the decision they made. That's their path.*\n\n"
        "**Check that you follow the rules.**"
    ),
    "technical": (
        "*No acting like a damn kid — do not embarrass our Technical name or me. Take this seriously.*\n\n"
        "**Check that you follow the rules.**"
    ),
    "janitor": "**Check that you follow the rules.**",
    "medical": (
        "I believe that anybody in my division will respect these rules and behave the right way, "
        "because I will not tolerate, nor have mercy for, **anyone** who doesn't follow these "
        "principal rules of RESPECT.\n\n"
        "I see every move and have eyes everywhere in the server and the community server. If I "
        "hear any of you breaks **my** rules, there will be actions taken — and as I said, "
        "**I won't be so merciful.**\n\n"
        "-# — Julius Caesar, High Physician, Medical"
    ),
}

POINT_INFO = (
    "• You may re-join only by *High Rank* approval.\n"
    "• You can apply with an apology.\n"
    "• Warnings/points are removed after 1 month.\n"
    "• If you get banned again, it will be **permanent with no excuse**."
)

PUNISHMENT_TABLE = (
    "**Minor rule break** — 1 pt → Verbal warning\n"
    "**Repeated minor breaks** — 2 pts → Written warning\n"
    "**Moderate offense** — 3 pts → 24-hour timeout\n"
    "**Serious offense** — 5 pts → 7-day timeout\n"
    "**6+ points total** → 7-day ban\n"
    "**Extreme offense** → Immediate ban\n"
    "**Ban evasion / repeat ban** → **Permanent ban, no excuse**"
)


def _accent() -> discord.Colour:
    return discord.Colour.dark_theme()


def build_reply(title: str, body: str) -> ui.LayoutView:
    """Build a full Components V2 panel in the same style as Security-Rules."""
    view = ui.LayoutView()
    container = ui.Container(accent_color=_accent())
    container.add_item(ui.TextDisplay(f"# {title}"))
    container.add_item(
        ui.TextDisplay(
            f'And most important thing, you must follow [Discord\'s Terms of Service]({COMMUNITY_GUIDELINES_URL})'
        )
    )
    container.add_item(
        ui.ActionRow(
            ui.Button(
                label="Community Guidelines",
                style=discord.ButtonStyle.link,
                url=COMMUNITY_GUIDELINES_URL,
            )
        )
    )
    container.add_item(ui.Separator())
    container.add_item(ui.TextDisplay(body))
    container.add_item(
        ui.TextDisplay(
            "> • If you have a problem or a question, open a ticket in support."
        )
    )

    support_button = ui.Button(
        label="Support",
        style=discord.ButtonStyle.link,
        url=SUPPORT_URL,
    )
    point_button = ui.Button(
        label="Point Info",
        style=discord.ButtonStyle.secondary,
        custom_id="wraith:general:point_info",
    )
    punish_button = ui.Button(
        label="Punishment Power",
        style=discord.ButtonStyle.secondary,
        custom_id="wraith:general:punishment",
    )

    async def point_callback(interaction: discord.Interaction):
        await interaction.response.send_message(
            view=build_reply("Point Info", POINT_INFO),
            ephemeral=True,
        )

    async def punish_callback(interaction: discord.Interaction):
        await interaction.response.send_message(
            view=build_reply("Punishment Power", PUNISHMENT_TABLE),
            ephemeral=True,
        )

    point_button.callback = point_callback
    punish_button.callback = punish_callback
    container.add_item(ui.ActionRow(point_button, punish_button, support_button))
    container.add_item(
        ui.TextDisplay(
            "> • You may re-join only by *High Rank* approval\n"
            "You can apply with an apology."
        )
    )
    container.add_item(
        ui.TextDisplay(
            "> • Your warnings with points will be removed after a month.\n"
            "If you get banned again, will be perm with no excuse."
        )
    )
    container.add_item(ui.Separator())
    container.add_item(
        ui.TextDisplay(
            "*General rules apply to every member. Serious violations may result in "
            "warning, mute, suspension, or ban depending on severity.*"
        )
    )
    container.add_item(ui.TextDisplay("-# Made by Saintless"))
    view.add_item(container)
    return view


def build_rule_detail(rule: dict) -> ui.LayoutView:
    view = ui.LayoutView()
    container = ui.Container(accent_color=_accent())
    container.add_item(ui.TextDisplay(f"# {rule['title']}"))
    container.add_item(ui.Separator())
    container.add_item(
        ui.TextDisplay("\n".join(f"> • {bullet}" for bullet in rule["bullets"]))
    )
    view.add_item(container)
    return view


def build_department_view(dept_key: str) -> ui.LayoutView:
    """Build the full Components V2 department panel with a persistent selector."""
    return DepartmentRulesView(dept_key)


class RuleSelect(ui.Select):
    def __init__(self, dept_key: str, rules: list[dict]):
        options = [
            discord.SelectOption(
                label=rule["label"],
                value=rule["value"],
                description=rule["description"],
            )
            for rule in rules
        ]
        super().__init__(
            placeholder="Select The Rule",
            custom_id=f"wraith:{dept_key}:select",
            options=options,
        )
        self.dept_key = dept_key

    async def callback(self, interaction: discord.Interaction):
        value = self.values[0]
        rule = next(
            (item for item in RULESETS[self.dept_key] if item["value"] == value),
            None,
        )
        if rule is None:
            await interaction.response.send_message(
                "Couldn't find that rule. Try again.",
                ephemeral=True,
            )
            return
        await interaction.response.send_message(
            view=build_rule_detail(rule),
            ephemeral=True,
        )


class DepartmentRulesView(ui.LayoutView):
    def __init__(self, dept_key: str):
        super().__init__(timeout=None)
        self.dept_key = dept_key
        rules = RULESETS[dept_key]

        container = ui.Container(accent_color=_accent())
        container.add_item(ui.TextDisplay(f"# {TITLES[dept_key]}"))
        container.add_item(
            ui.TextDisplay(
                f'And most important thing, you must follow [Discord\'s Terms of Service]({COMMUNITY_GUIDELINES_URL})'
            )
        )
        container.add_item(
            ui.ActionRow(
                ui.Button(
                    label="Community Guidelines",
                    style=discord.ButtonStyle.link,
                    url=COMMUNITY_GUIDELINES_URL,
                )
            )
        )
        container.add_item(ui.Separator())
        container.add_item(
            ui.TextDisplay(
                'Click **"Select The Rule"** to read the rules. They\'re important too.\n'
                'If it gives error **"This interaction failed"** try again.'
            )
        )
        container.add_item(ui.ActionRow(RuleSelect(dept_key, rules)))
        container.add_item(
            ui.TextDisplay(
                "> • If you have a problem or a question, open a ticket in support."
            )
        )

        point_button = ui.Button(
            label="Point Info",
            style=discord.ButtonStyle.secondary,
            custom_id=f"wraith:{dept_key}:point_info",
        )
        punish_button = ui.Button(
            label="Punishment Power",
            style=discord.ButtonStyle.secondary,
            custom_id=f"wraith:{dept_key}:punishment",
        )
        support_button = ui.Button(
            label="Support",
            style=discord.ButtonStyle.link,
            url=SUPPORT_URL,
        )
        point_button.callback = self.on_point_info
        punish_button.callback = self.on_punishment
        container.add_item(ui.ActionRow(point_button, punish_button, support_button))

        container.add_item(
            ui.TextDisplay(
                "> • You may re-join only by *High Rank* approval\\n"
                "You can apply with an apology."
            )
        )
        container.add_item(
            ui.TextDisplay(
                "> • Your warnings with points will be removed after a month.\\n"
                "If you get banned again, will be perm with no excuse."
            )
        )
        container.add_item(ui.Separator())
        container.add_item(ui.TextDisplay(CLOSING_TEXT[dept_key]))
        container.add_item(ui.TextDisplay("-# Made by Saintless"))

        self.add_item(container)

    async def on_point_info(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            view=build_reply("Point Info", POINT_INFO),
            ephemeral=True,
        )

    async def on_punishment(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            view=build_reply("Punishment Power", PUNISHMENT_TABLE),
            ephemeral=True,
        )


def build_persistent_department_views() -> list[DepartmentRulesView]:
    """Return one persistent view per department for restart-safe interactions."""
    return [DepartmentRulesView(key) for key in RULESETS]


