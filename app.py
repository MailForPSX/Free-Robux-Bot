import os
import asyncio
from flask import Flask
from threading import Thread
from logger import log_it
from secret import cookie
import pytchat
import requests
from random import choice
from json import dumps
from time import time

app = Flask('')

@app.route('/')
def home():
    return "Bot is running!"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    Thread(target=run_web).start()

# (Include your get_gamepass, delete_buy, main functions here from your original code)

async def main():
    # Your bot logic here, as in your original code
    pass

if __name__ == '__main__':
    keep_alive()
    asyncio.run(main())
