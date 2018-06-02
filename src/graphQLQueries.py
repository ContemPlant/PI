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


def add_sensor_data_queryfn(obj: dict) -> str:
    """
    Generates query to add sensor data out of object values

    :param obj: sensor date object
    :return:  graphql query to insert sensor date
    """
    return f'''
    addSensorData(
            type: {obj['type']}
            value: {obj['value']}
            timeStamp: {obj['timestamp']}
            arduId: {obj['arduId']}
        ) {{ id }}
    '''


#
def subscribe_to_ardu_change_query() -> json:
    """
    Generates query to subscribe to changes in ardu table

    :return:  subscription query
    """
    return json.dumps({
        "type": "subscription_start",
        "query": """subscription {
        arduChange {
            mutation
            node {
                arduId
                loadedPlant {
                    temperature_opt
                    radiation_opt
                    humidity_opt
                    loudness_opt
                    temperature_weight
                    radiation_weight
                    humidity_weight
                    loudness_weight
                }
            }
        }
    }"""
    })
