import os

from telethon import TelegramClient
import configparser

config = configparser.ConfigParser()

if os.path.exists('config_prod.ini'):
    config.read('config_prod.ini')
else:
    config.read('config.ini')

api_id = config['user_bot']['api_id']
api_hash = config['user_bot']['api_hash']

client = TelegramClient('anon', api_id, api_hash)


async def main():
    me = await client.get_me()
    print(me.stringify())


with client:
    client.loop.run_until_complete(main())

