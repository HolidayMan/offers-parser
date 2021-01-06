import telethon
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

api_id = config['user_bot']['api_id']
api_hash = config['user_bot']['api_hash']


