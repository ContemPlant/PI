import datetime
from sensordata import sensorDates
from graphQLClient import GraphQLClient
from graphQLQueries import addSensorDataQueryfn

# plantsDbEndpoint = 'http://167.99.240.197:8000/graphql'
plantsDbEndpoint = 'http://localhost:8000/graphql'

client = GraphQLClient(plantsDbEndpoint)


def datesToQuery(date):
    # unpack all the parameters that we receive
    flags, pid, aid, timestamp, phealth, psize, temp, hum, rad = date

    # Hard code timestamp and ardu id for now
    timestamp = datetime.datetime.now().isoformat()
    aid = "cjh51fk31001z07497emu90xa"

    # Associate values with types
    types_values = [('TEMP', temp), ('HUM', hum), ('RAD', rad)]

    # Build query vars
    return [sensorToObj(t, v, timestamp, aid) for t, v in types_values]


def sensorToObj(type, value, timestamp, arduId):
    return {
        "type": type,
        "value": value,
        "timestamp": f'"{timestamp}"',
        "arduId": f'"{arduId}"'
    }

# Get all the dates
for dates in sensorDates():
    # Build query from dates
    query = datesToQuery(dates)
    # Execute
    client.executeMultiple(addSensorDataQueryfn, query)