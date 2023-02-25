import os
import logging


logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


class Config(object):
    # Get a bot token from @botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5897885316:AAH-aL9uCAWnClzNtM72EihMvkv28vkEzvo")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", "10038985"))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "b13a9434d5f59fdb592bf3cd0f457eff")

    # Authorized users to use this bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1187675214").split())

    # session name
    TG_USER_SESSION_NAME = os.environ.get("TG_USER_SESSION_NAME", "oxmohsen")

    # tg user session string
    TG_USER_SESSION_STRING = os.environ.get("TG_USER_SESSION_STRING", "")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
