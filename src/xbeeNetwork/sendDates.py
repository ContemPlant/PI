import datetime
from xbeeNetwork.arduCom import sensor_dates
from backendConnect.graphQLClient import GraphQLClient
from backendConnect.graphQLQueries import add_sensor_data_queryfn
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


def send_dates(device):
    print("Ready to receive sensor dates")

    # Get all the dates
    for dates in sensor_dates(device):
        print(dates)
        # Build query from dates
        query = dates_to_query(dates)
        # Execute
        client.execute(query)
