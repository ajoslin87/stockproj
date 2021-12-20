from aiohttp import web
import socketio
import os
# from yahoo_fin import stock_info as si
# from yahoo_fin import get_quote_table as qt
import paho.mqtt.client as mqtt
import time 
import datetime
import json
import pandas as pd
from flask import Flask, render_template, url_for, request

# from querystock import querystock


# from yahoo_fin import stock_info as si
# # from yahoo_fin import get_quote_table as qt
# import paho.mqtt.client as mqtt
# import time 
# import datetime
# import json
# import pandas as pd

socket_io = socketio.AsyncServer(cors_allowed_origins='*')

web_app = web.Application()

socket_io.attach(web_app)

breakPoint = False

fuckShit = True 

#define endpoints 
async def index(request):
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, './templates/index.html')
    with open(filename) as file_obj:
        return web.Response(text = file_obj.read(), content_type='text/html')

@socket_io.on('message')
async def print_message(id, message):
    print("socket id is {}".format(id))
    print(message)
    #enabling two-way communication
    await socket_io.emit('message', "you said {}".format(message))
    # querystock(message)




#bind the aiohttp endpoint to the web_application
web_app.router.add_get('/',index)

#start the server
if __name__ == '__main__':
    web.run_app(web_app)