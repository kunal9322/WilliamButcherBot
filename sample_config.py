import os

BOT_TOKEN = os.environ.get('BOT_TOKEN','6221284663:AAGop_cKtr03r4Tv8k7NeDpV4lb0X1uLGck')
API_ID = 16743442) 
SESSION_STRING = os.environ.get('SESSION_STRING', '')
API_HASH = os.environ.get('API_HASH','12bbd720f4097ba7713c5e40a11dfd2a')
USERBOT_PREFIX = os.environ.get('USERBOT_PREFIX', '.')
PHONE_NUMBER = os.environ.get('PHONE_NUMBER')
SUDO_USERS_ID = list(map(int, os.environ.get('SUDO_USERS_ID', '5885920877').split()))
LOG_GROUP_ID = int(os.environ.get('LOG_GROUP_ID','-1001710461452'))
GBAN_LOG_GROUP_ID = int(os.environ.get('GBAN_LOG_GROUP_ID','-1001710461452'))
MESSAGE_DUMP_CHAT = int(os.environ.get('MESSAGE_DUMP_CHAT','-1001710461452'))
WELCOME_DELAY_KICK_SEC = int(os.environ.get('WELCOME_DELAY_KICK_SEC', 600))
MONGO_URL = os.environ.get('MONGO_URL','mongodb+srv://sonu55:sonu55@cluster0.vqztrvk.mongodb.net/?retryWrites=true&w=majority')
ARQ_API_KEY = os.environ.get('ARQ_API_KEY')
ARQ_API_URL = os.environ.get('ARQ_API_URL', 'https://arq.hamker.in')
LOG_MENTIONS = os.environ.get('LOG_MENTIONS', 'True').lower() in ['true', '1']
RSS_DELAY = int(os.environ.get('RSS_DELAY', 300))
PM_PERMIT = os.environ.get('PM_PERMIT', 'True').lower() in ['true', '1']
