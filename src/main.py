from sensordata import sensorDates
from graphQLClient import GraphQLClient
from graphQLQueries import addSensorDataQueryfn

# plantsDbEndpoint = 'http://167.99.240.197:8000/graphql'
plantsDbEndpoint = 'http://localhost:8000/graphql'

# for date in sensorDates():
#     print(date)

client = GraphQLClient(plantsDbEndpoint)

client.executeMultiple(addSensorDataQueryfn, [{
    'type': 'TEMP',
    'value': '14',
    'timestamp': '"2018-05-13T16:28:35+00:00"',
    'arduId': '"cjh51fk31001z07497emu90xa"'
}, {
    'type': 'HUM',
    'value': '20',
    'timestamp': '"2018-05-13T16:28:35+00:00"',
    'arduId': '"cjh51fk31001z07497emu90xa"'
}])
