import os
from typing import List

API_ID = os.environ.get("API_ID", "21757905")
API_HASH = os.environ.get("API_HASH", "5631e91f55477ccbe38e373643dd11ae")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8224976419:AAH3SoCoH7yTN4acyqEDC_-gZdqbgUmxg3U")
ADMIN = int(os.environ.get("ADMIN", "2057229350"))
PICS = (os.environ.get("PICS", "https://i.ibb.co/MDssddJp/pic.jpg https://i.ibb.co/n8fQ2xcx/pic.jpg")).split()
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002633593906"))
NEW_REQ_MODE = os.environ.get("NEW_REQ_MODE", "True").lower() == "true"
DB_URI = os.environ.get("DB_URI", "mongodb+srv://sridharlogavani2003_db_user:ELcllQ53CaZYMqOU@cluster0.b0hnfs9.mongodb.net/?appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "cluster0")
IS_FSUB = os.environ.get("IS_FSUB", "True").lower() == "true"  # Set "True" For Enable Force Subscribe
AUTH_CHANNELS = list(map(int, os.environ.get("AUTH_CHANNELS", "-1004291365290").split())) # Add Multiple channel ids
AUTH_REQ_CHANNELS = list(map(int, os.environ.get("AUTH_REQ_CHANNELS", "-1004291365290").split())) # Add Multiple channel ids
FSUB_EXPIRE = int(os.environ.get("FSUB_EXPIRE", 2))  # minutes, 0 = no expiry
PING_URL = os.environ.get("PING_URL", "") # Service URL for Keep-Alive
VERSION = os.environ.get("VERSION", "3.0")
