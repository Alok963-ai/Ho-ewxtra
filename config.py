#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "20288951"))
API_HASH = environ.get("API_HASH", "e8cb5fb7a475b5f5eb3b0ef0e6ca03a8")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
AUTH_USER = os.environ.get('AUTH_USERS', '7833842279').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
HOST = "https://drm-api-six.vercel.app"
CREDIT = "kaka"
ADMIN_ID = [7833842279]
DB_NAME = "alokjangde6"
DB_URL = "mongodb+srv://alokjangde6:Sapnaipali71$@cluster0.cx60pkr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
LOG_CHANNEL = -1002548493129 # Your Log Channel ID (Bot ko ADMIN BNAYE)
USERLINK = "t.me/Alliswell71"
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
