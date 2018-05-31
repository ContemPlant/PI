import asyncio  # for async/await
import websockets  # websockets...
import json  # json parsing
from pprint import pprint  # pretty printing
from graphQLQueries import subscribeToArduChangeQuery  # subscrube query
from parsing import parseToLoadPlantBytes, loadPlantObjectToTuple
from arduSend import sendData
from constants import API_ADDR_SUB


async def onPlantLoaded():
    protocol = "graphql-subscriptions"

    async with websockets.connect(API_ADDR_SUB, subprotocols=[protocol]) as websocket:
        await websocket.send(subscribeToArduChangeQuery())
        while True:
            data = await websocket.recv()
            node = json.loads(data)['payload']['data']['arduChange']['node']
            yield node


async def main(device):
    async for change in onPlantLoaded():
        arduId = 'A' + change['arduId']

        print(arduId)
        plant = change['loadedPlant']
        pprint(plant)

        plantTuple = loadPlantObjectToTuple(plant)
        dem_bytes = parseToLoadPlantBytes(plantTuple)
        sendData(arduId, dem_bytes, device)


def subscribtion(device):
    print("Starting async loop")
    loop = asyncio.new_event_loop()
    # Blocking call which returns when the main() coroutine is done
    loop.run_until_complete(main(device))
    loop.close()
