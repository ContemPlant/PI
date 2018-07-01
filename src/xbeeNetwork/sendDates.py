import datetime
from xbeeNetwork.arduCom import ardu_messages
from backendConnect.graphQLClient import GraphQLClient
from backendConnect.graphQLQueries import add_sensor_data_queryfn, unload_plant_query
from constants import API_ADDR_QM

client = GraphQLClient(API_ADDR_QM)


def dates_to_query(date):
    # unpack all the parameters that we receive
    flags, aid, timestamp, compression, temp, hum, rad, loud = date

    # Hard code timestamp and ardu id for now
    timestamp = datetime.datetime.now().isoformat()
    aid = str(aid).zfill(4)

    # Build query vars
    return add_sensor_data_queryfn(temp, hum, rad, loud, timestamp, aid)


def send_dates(dates):
    # Build query from dates
    query = dates_to_query(dates)
    # Execute
    return client.execute(query)


def unload_plant(message):
    # unpack the source (ardu id)
    aid = str(message[1]).zfill(4)
    query = unload_plant_query(ardu_id=aid)
    return client.execute(query)


def handle_messages(device):
    print("Ready to receive sensor dates")

    # Get all the dates
    for message in ardu_messages(device):
        print(message)
        flag = message[0]

        if flag == 1: send_dates(message)
        if flag == 2: unload_plant(message)
