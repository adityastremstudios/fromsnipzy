TORTOISE = {
    "connections": {
         "default": "postgres://postgres.mfssjedxowpuwmkqtfuh:PSe#$885$#@aws-1-us-east-1.pooler.supabase.com:5432/postgres",
     
    },
    "apps": {
        "models": {
            "models": [
                "models.misc",
                "models", 
                "aerich.models"
            ],
            "default_connection": "default",
        }
    }
}


EXTENSIONS = [
    "cogs.esports",
    "cogs.events",
    "cogs.mod",
    "cogs.premium",
    "cogs.quomisc",
    "cogs.reminder",
    "cogs.utility",
]


DISCORD_TOKEN = "MTQzNDQ0NjY5NDE5OTcyMjA1NA.GwK-ap.YWxSxagGONqsIUbR-Ge3m5TIz2EVpV0jCKquVU"


COLOR = 0x00FFB3
FOOTER = "Punisher Scrims"
PREFIX = "q"
PRIME_EMOJI = "🫰"
OWNER_ID = "1303527224229625858"
DEVS = [1397832329237630986, ]

SERVER_LINK = "https://discord.gg/qKQ4ghCydN"
SERVER_ID =  "1434446745798185081"
TOURNEY_CSV_CHANNEL = "1436362553914687490"
EMOJIS_SERVER = [1434446745798185081, 1437003468660539477] 

BOT_INVITE = "https://discord.com/oauth2/authorize?client_id=1434446694199722054&permissions=8&integration_type=0&scope=bot+applications.commands"

ACTIVITIES = [
    {"type": "playing", "name": "scrims across Punisher eSports"},
]
# ─────────────────────────────────────────────────────────────
#  Activity Placeholders (usable in "name" field)
#  These will automatically update with live bot stats.
#
#  Available Placeholders:
#    {servers}   → Total number of servers the bot is in
#    {members}   → Sum of all members across all servers
#    {msgs}      → Total messages seen since startup
#    {uptime}    → Current uptime in human-readable format
#    {cmds}      → Total commands executed since startup
#
#  Example:
#    {"type": "playing", "name": "serving {servers} communities"}
# ─────────────────────────────────────────────────────────────


# LOGS
SHARD_LOG = "https://discord.com/api/webhooks/1437004802826436662/lMkawPZyAFqnU1HieyBlztmvF0-RIf7k8L7wWBgwjOwieqJB-tzm9lAwF1z2TGLJqi82"
ERROR_LOG = "https://discord.com/api/webhooks/1437004981851918378/4w-RnYU8gcxZwq89ymDjPbMWlza1ELVEjcl4UgZ-k8CesKt6BcoTTDpHrmS5p7jn4kGQ"
PUBLIC_LOG = "https://discord.com/api/webhooks/1437005108071370924/tIj9SGDlxrMkNDxYmf91tcOFLmzeulA9rUqNZiiad_-G4y2XnCnZvdGSUexmwP39P9nf"

