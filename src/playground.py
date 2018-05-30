import asyncio                                          # for async/await
import websockets                                       # websockets...
import json                                             # json parsing
from pprint import pprint                               # pretty printing
from graphQLQueries import subscribeToArduChangeQuery   # subscrube query

URL = "ws://localhost:8000/subscriptions"
PROTO = ["graphql-subscriptions"]


async def onPlantLoaded():
    async with websockets.connect(URL, subprotocols=PROTO) as websocket:
        await websocket.send(subscribeToArduChangeQuery())
        while True:
            data = await websocket.recv()
            node = json.loads(data)['payload']['data']['arduChange']['node']
            yield node


async def main():
    async for change in onPlantLoaded():
        arduID = change['arduId']
        plant = change['loadedPlant']
        pprint(plant)

asyncio.get_event_loop().run_until_complete(main())
