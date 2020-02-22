class Config(object):
    LOGGER = False

    # REQUIRED
    API_KEY = ""
    OWNER_ID = "995737497"  # If you dont know, run the bot and do /id in your private chat with it
    OWNER_USERNAME = "Linux_404"

    # RECOMMENDED
    SQLALCHEMY_DATABASE_URI = None  # needed for any database modules
    MESSAGE_DUMP = None  # needed to make sure 'save from' messages persist
    LOAD = []
    NO_LOAD = ['translation', 'sed']
    WEBHOOK = 'ANYTHING'
    URL = None

    # OPTIONAL
    SUDO_USERS = []  # List of id's (not usernames) for users which have sudo access to the bot.
    SUPPORT_USERS = []  # List of id's (not usernames) for users which are allowed to gban, but can also be banned.
    WHITELIST_USERS = []  # List of id's (not usernames) for users which WONT be banned/kicked by the bot.
    MAPS_API = ''
    CERT_PATH = None
    PORT = 4728
    DEL_CMDS = True  # Whether or not you should delete "blue text must click" commands
    STRICT_ANTISPAM = True
    WORKERS = 8  # Number of subthreads to use. This is the recommended amount - see for yourself what works best!
    BAN_STICKER = ''  # banhammer marie sticker
    STRICT_GBAN = True
    STRICT_GMUTE = True
    ALLOW_EXCL = True  # Allow ! commands as well as /
    API_OPENWEATHER = ''  # OpenWeather API

    # MEMES
    DEEPFRY_TOKEN = None


class Production(Config):
    LOGGER = False


class Development(Config):
    STRICT_GMUTE = True
    DONATION_LINK = True
    LOGGER = True
