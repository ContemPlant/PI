import asyncio  # for async/await
import websockets  # websockets...
import json  # json parsing
from pprint import pprint  # pretty printing
from backendConnect.graphQLQueries import subscribe_to_ardu_change_query  # subscrube query
from parsing import parse_to_load_plant_bytes
from xbeeNetwork.arduCom import send_data
from constants import API_ADDR_SUB


# Generator for subscription changes
async def on_plant_loaded():
    protocol = "graphql-subscriptions"

    # open socket
    async with websockets.connect(API_ADDR_SUB, subprotocols=[protocol]) as websocket:
        # await sending of query
        await websocket.send(subscribe_to_ardu_change_query())
        print("Making subscription")
        while True:
            # wait for subscription update
            data = await websocket.recv()
            print(data)
            node = json.loads(data)['payload']['data']['arduChange']['node']
            yield node


async def main(device):
    async for change in on_plant_loaded():
        ardu_id = 'A' + change['arduId']

        plant = change['loadedPlant']
        print(f"Loading plant {plant['name']} on {ardu_id}")

        dem_bytes = parse_to_load_plant_bytes(plant)
        send_data(ardu_id, dem_bytes, device)


def subscription(device):
    print("Starting async loop")
    loop = asyncio.new_event_loop()
    # Blocking call which returns when the main() coroutine is done
    loop.run_until_complete(main(device))
    loop.close()
