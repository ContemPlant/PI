import datetime
from xbeeNetwork.arduCom import sensor_dates
from backendConnect.graphQLClient import GraphQLClient
from backendConnect.graphQLQueries import add_sensor_data_queryfn
from constants import API_ADDR_QM
from parsing import sensor_tuple_to_object

client = GraphQLClient(API_ADDR_QM)


def dates_to_query(date):
    # unpack all the parameters that we receive
    flags, sid, timestamp, compression, temp, hum, rad, loud = date

    # Hard code timestamp and ardu id for now
    timestamp = datetime.datetime.now().isoformat()
    # aid = "cjhbrl7jb00bu0762shs2yo3g"
    sid = str(sid).zfill(4)

    # Associate values with types
    types_values = [('TEMP', temp), ('HUM', hum), ('RAD', rad), ('LOUD', loud)]

    # Build query vars
    return [sensor_tuple_to_object(t, v, timestamp, sid) for t, v in types_values]


def send_dates(device):
    print("Ready to receive sensor dates")

    # Get all the dates
    for dates in sensor_dates(device):
        # Build query from dates
        query = dates_to_query(dates)
        print(dates)
        # Execute
        client.executeMultiple(add_sensor_data_queryfn, query)
