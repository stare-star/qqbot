import os
import sys
from os import path

import nonebot

import config

nonebot.init(config)
nonebot.load_plugins(
    path.join(path.dirname(__file__), 'awesome', 'plugins'),
    'awesome.plugins'
)
bot = nonebot.get_bot()
app = bot.asgi

if __name__ == '__main__':
    bot.run(port=8080)
