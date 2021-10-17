import os
from os import getenv

from dotenv import load_dotenv

from helpers.uptools import fetch_heroku_git_url

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
que = {}
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "ᴅᴀᴄᴄʜᴜ")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/3dd9c9e061fbc5c114833.jpg")
THUMB_IMG = getenv("THUMB_IMG", "https://telegra.ph/file/3dd9c9e061fbc5c114833.jpg")
AUD_IMG = getenv("AUD_IMG", "https://telegra.ph/file/3dd9c9e061fbc5c114833.jpg")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/5aa50f1f5315ee259a409.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/3dd9c9e061fbc5c114833.jpg")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME", "DacchuMusicBot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Dacchu_xD")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "DacchuX_Support")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Dacchulive")
OWNER_NAME = getenv("OWNER_NAME", "XDacchuX")
PMPERMIT = getenv("PMPERMIT", "ENABLE")
# fill with your id as the owner of the bot
OWNER_ID = int(os.environ.get("OWNER_ID"))
#fill there Ur Account username
ALIVE_NAME = getenv("ALIVE_NAME", "XDacchuX")
DATABASE_URL = os.environ.get("DATABASE_URL")  # fill with your mongodb url
# make a private channel and get the channel id
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL"))
# just fill with True or False (optional)
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
# UPDATER CONFIG
U_BRANCH = "main"
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
UPSTREAM_REPO = os.environ.get(
    "UPSTREAM_REPO", "https://github.com/XDacchuX/Dacchu-Vc-player"
)
HEROKU_URL = fetch_heroku_git_url(HEROKU_API_KEY, HEROKU_APP_NAME)
