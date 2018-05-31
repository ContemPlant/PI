import datetime
from sensorData import sensorDates, sensorToObj
from graphQLClient import GraphQLClient
from graphQLQueries import addSensorDataQueryfn
from constants import API_ADDR_QM

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
    return [sensorToObj(t, v, timestamp, sid) for t, v in types_values]


def send_dates(device):
    print("Ready to receive sensor dates")

    # Get all the dates
    for dates in sensorDates(device):
        # Build query from dates
        query = dates_to_query(dates)
        print(dates)
        # Execute
        client.executeMultiple(addSensorDataQueryfn, query)
