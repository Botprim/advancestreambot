# (c) adarsh-goel
import os
from os import getenv, environ
from dotenv import load_dotenv

load_dotenv()

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv('API_ID', '27116256'))
    API_HASH = str(getenv('API_HASH', '89669f3ecf7d5257926a50701371100b'))
    BOT_TOKEN = str(getenv('BOT_TOKEN', '6620784685:AAGLKiPLBWNlnBBEwcOSL-SZV-TEl1g_0yQ'))
    name = str(getenv('name', 'filetolinkbot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1003550063769'))
    PORT = int(getenv('PORT', 8080))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "8336815364").split())  
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    OWNER_USERNAME = str(getenv('OWNER_USERNAME', 'Sumit_uv'))

    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    else:
        ON_HEROKU = False

    FQDN = str(getenv('FQDN', 'advancestreambot-11kq.onrender.com')) if not ON_HEROKU or getenv('FQDN') else APP_NAME + '.herokuapp.com'
    HAS_SSL = bool(getenv('HAS_SSL', False))

    if HAS_SSL:
        URL = "https://advancestreambot-11kq.onrender.com/".format(FQDN)
    else:
        URL = "https://advancestreambot-11kq.onrender.com/".format(FQDN)

    DATABASE_URL = str(getenv('DATABASE_URL', 'mongodb+srv://Marvelbotz:Marvelbotz@cluster0.oyxdumi.mongodb.net/?retryWrites=true&w=majority'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', 'marvelbackupp'))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1001362659779")).split())) 
    SHORTLINK_URL = getenv('SHORTLINK_URL', 'linkcents.com')
    SHORTLINK_API = getenv('SHORTLINK_API', '84a3e44eb56e270b5f8eb969e1f13d8098b2a60d')
    TUTORIAL_URL = getenv('TUTORIAL_URL', 'https://t.me/marvelsbackup/3')
