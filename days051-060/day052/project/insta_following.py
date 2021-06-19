import os

from insta_follower import InstaFollower

CHROMEDRIVER_PATH = os.getenv('CHROMEDRIVER_PATH')
SIMILAR_ACCOUNT = 'pullynnhah'
USERNAME = os.getenv('INSTAGRAM_USER')
PASSWORD = os.getenv('INSTAGRAM_PASS')

bot = InstaFollower(CHROMEDRIVER_PATH)
bot.login(USERNAME, PASSWORD)
bot.find_follower(SIMILAR_ACCOUNT)
bot.follow()
del bot
