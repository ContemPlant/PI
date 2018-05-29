#!/usr/bin/env python

# WS client example

import asyncio
import websockets
from graphQLQueries import subscribeToArduChangeQuery

URL = "ws://localhost:8000/subscriptions"
PROTO = ["graphql-subscriptions"]

async def onPlantLoaded():

    async with websockets.connect(URL, subprotocols=PROTO) as websocket:
        await websocket.send(subscribeToArduChangeQuery())

        ret = await websocket.recv()
        yield ret

async def main():

    async for change in onPlantLoaded():
        print(change)

asyncio.get_event_loop().run_until_complete(main())
