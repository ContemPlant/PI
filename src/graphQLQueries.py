# mutation($type: SensorType!, $value: Float!, $timestamp: DateTime!,
# $arduId: ID!) {
#     addSensorData(
#         type: $type
#         value: $value
#         timeStamp: $timestamp
#         arduId: $arduId
#     ) { id }
# }
import json


def addSensorDataQueryfn(obj):
    return f'''
    addSensorData(
            type: {obj['type']}
            value: {obj['value']}
            timeStamp: {obj['timestamp']}
            arduId: {obj['arduId']}
        ) {{ id }}
    '''


def subscribeToArduChangeQuery():
    return json.dumps({
        "type": "subscription_start",
        "query": """subscription {
        arduChange {
            mutation
            node {
                arduId
                loadedPlant {
                    name
                }
            }
        }
    }"""
    })
