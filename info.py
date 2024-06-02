import re
from os import environ
from Script import script

def is_enabled(type, value):
    data = environ.get(type, str(value))
    if data.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif data.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        print(f'Error - {type} is invalid, exiting now')
        exit()

def is_valid_ip(ip):
    ip_pattern = r'\b(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b'
    return re.match(ip_pattern, ip) is not None

# Bot information
API_ID = environ.get('API_ID', '')
if len(API_ID) == 0:
    print('Error - API_ID is missing, exiting now')
    exit()
else:
    API_ID = int(API_ID)
API_HASH = environ.get('API_HASH', '')
if len(API_HASH) == 0:
    print('Error - API_ID is missing, exiting now')
    exit()
BOT_TOKEN = environ.get('BOT_TOKEN', '')
if len(BOT_TOKEN) == 0:
    print('Error - BOT_TOKEN is missing, exiting now')
    exit()
PORT = int(environ.get('PORT', '8080'))

# Bot pics
PICS = (environ.get('PICS', 'https://telegra.ph/file/58fef5cb458d5b29b0186.jpg https://telegra.ph/file/f0aa4f433132769f8970c.jpg https://telegra.ph/file/f515fbc2084592eca60a5.jpg https://telegra.ph/file/20dbdcffaa89bd3d09a74.jpg https://telegra.ph/file/6045ba953af4def846238.jpg')).split()

# Bot Admins
ADMINS = environ.get('ADMINS', '2023517850')
if len(ADMINS) == 0:
    print('Error - ADMINS is missing, exiting now')
    exit()
else:
    ADMINS = [int(admins) for admins in ADMINS.split()]

# Channels
INDEX_CHANNELS = [int(index_channels) if index_channels.startswith("-") else index_channels for index_channels in environ.get('INDEX_CHANNELS', '-1001719548150').split()]
if len(INDEX_CHANNELS) == 0:
    print('Info - INDEX_CHANNELS is empty')
LOG_CHANNEL = environ.get('LOG_CHANNEL', '')
if len(LOG_CHANNEL) == 0:
    print('Error - LOG_CHANNEL is missing, exiting now')
    exit()
else:
    LOG_CHANNEL = int(LOG_CHANNEL)
    
SUPPORT_GROUP = environ.get('SUPPORT_GROUP', '-1001918925906')
if len(SUPPORT_GROUP) == 0:
    print('Error - SUPPORT_GROUP is missing, exiting now')
    exit()
else:
    SUPPORT_GROUP = int(SUPPORT_GROUP)

# MongoDB information
DATABASE_URL = environ.get('DATABASE_URL', "")
if len(DATABASE_URL) == 0:
    print('Error - DATABASE_URL is missing, exiting now')
    exit()
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Files')

# Links
SUPPORT_LINK = environ.get('SUPPORT_LINK', 'https://t.me/mybotsupport')
UPDATES_LINK = environ.get('UPDATES_LINK', 'https://t.me/moviez_areas')
FILMS_LINK = environ.get('FILMS_LINK', 'https://t.me/+cikLkbDz4T01N2Q1')


# Bot settings
AUTO_FILTER = is_enabled((environ.get('AUTO_FILTER', "True")), True)
IMDB = is_enabled((environ.get('IMDB', "False")), False)
SPELL_CHECK = is_enabled(environ.get("SPELL_CHECK", "True"), True)
SHORTLINK = is_enabled((environ.get('SHORTLINK', "True")), True)
DELETE_TIME = int(environ.get('DELETE_TIME', '2000')) # Add time in seconds
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
WELCOME = is_enabled((environ.get('WELCOME', "False")), False)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
LINK_MODE = is_enabled(environ.get("LINK_MODE", "True"), True)
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
MAX_BTN = int(environ.get('MAX_BTN', 10))
PAYMENT_QR = environ.get('PAYMENT_QR', 'https://graph.org/file/46fd33d87206259d3071b.jpg')
LANGUAGES = [language.lower() for language in environ.get('LANGUAGES', 'tam hin tel kan mal eng multi dual').split()]
QUALITY = [quality.lower() for quality in environ.get('QUALITY', '360p 480p 720p 1080p 2160p').split()]
PM_FILE_DELETE_TIME = int(environ.get('PM_FILE_DELETE_TIME', 1200))

# Other
IS_PM_SEARCH = is_enabled('IS_PM_SEARCH', True)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", script.IMDB_TEMPLATE)
FILE_CAPTION = environ.get("FILE_CAPTION", script.FILE_CAPTION)
SHORTLINK_URL = environ.get("SHORTLINK_URL", "moneykamalo.com")
SHORTLINK_API = environ.get("SHORTLINK_API", "60194c2494812fa1ac565d03aa1e6975b790aa1f")
VERIFY_EXPIRE = int(environ.get('VERIFY_EXPIRE', "3600")) # Add time in seconds
IS_VERIFY = is_enabled(environ.get("IS_VERIFY", "False"), False)
WELCOME_TEXT = environ.get("WELCOME_TEXT", script.WELCOME_TEXT)
TUTORIAL = environ.get("TUTORIAL", "https://t.me/how_to_openlinkz/19")
VERIFY_TUTORIAL = environ.get("VERIFY_TUTORIAL", "https://t.me/how_to_openlinkz/19")
INDEX_EXTENSIONS = [extensions.lower() for extensions in environ.get('INDEX_EXTENSIONS', 'mp4 mkv').split()]

#premium info
PAYMENT_QR = environ.get('PAYMENT_QR', 'https://telegra.ph/Payment-Information-02-03-5')
OWNER_UPI_ID = environ.get('OWNER_UPI_ID', 'p.satiz004@oksbi')
OWNER_USERNAME = environ.get("OWNER_USERNAME", "https://t.me/Itz_me_444")

#start_command_reactions
REACTIONS = ["😇", "🤗", "😍", "👍", "🥰", "😱", "😘", "⚡️"]

# stream features vars
IS_STREAM = is_enabled('IS_STREAM', False)
BIN_CHANNEL = environ.get("BIN_CHANNEL", "-1001930197257")
if len(BIN_CHANNEL) == 0:
    print('Error - BIN_CHANNEL is missing, exiting now')
    exit()
else:
    BIN_CHANNEL = int(BIN_CHANNEL)
URL = environ.get("URL", "https://professor-gva9.onrender.com")
if len(URL) == 0:
    print('Error - URL is missing, exiting now')
    exit()
else:
    if URL.startswith('https://'):
        if not URL.endswith("/"):
            URL += '/'
    elif '.' in URL:
        URL = f'http://{URL}:{PORT}/'
    else:
        print('Error - URL is not valid, exiting now')
        exit()
