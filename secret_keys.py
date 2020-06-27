import os
from dotenv import load_dotenv

load_dotenv()
DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
MONGODB_CONNECTION = os.getenv('MONGODB_CONNECTION')

LF_API_KEY = os.getenv('LF_API_KEY')
LF_API_SECRET = os.getenv('LF_API_SECRET')

OPENWEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY')

IG_USERNAME = os.getenv('IG_USERNAME')
IG_PASSWORD = os.getenv('IG_PASSWORD')
