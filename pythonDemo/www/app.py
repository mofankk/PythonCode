import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time 
from datetime import datetime

from aiohttp import www

def index(request):
    return web.Response(body=b'<h1>Hello,World<hq>')

@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_router("GET", "/", index)
    src = yield from loop.create_server(app.make_handler(), "127.0.0.1", 9000)
    logging.info("server started at http://127.0.0.1:8000")
    return srv 

loop = asynio.get_event_loop()
loop.run_util_complete(init(loop))
