import json


def add_sensor_data_queryfn(temperatureValue, humidityValue, radiationValue, loudnessValue, timeStamp, arduId) -> str:
    """
    Generates query to add sensor dates out of object values

    :param obj: sensor dates object
    :return:  graphql query to insert sensor dates
    """
    return f'''mutation {{
        addSensorDates(
            input: {{
                temperatureValue: {temperatureValue}
                humidityValue: {humidityValue}
                radiationValue: {radiationValue}
                loudnessValue: {loudnessValue}
                timeStamp: "{timeStamp}"
                arduId: "{arduId}"
            }}
        ) {{ id }}
    }}'''


def plant_state_query(plant_id):
    return f'''
    query {{
      plant(where: {id: "${plant_id}"}) {{
        plantStates {{
          health
          size
          environment
          sensorDates {{
            radiationValue
            loudnessValue
            humidityValue
            temperatureValue
            timeStamp
          }}
        }}
      }}'''

def subscribe_to_ardu_change_query() -> json:
    """
    Generates query to subscribe to changes in ardu table

    :return:  subscription query
    """
    return json.dumps({
        "type": "subscription_start",
        "query": """subscription {
        arduChange {
            node {
                arduId
                loadedPlant {
                    name
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


def unload_plant_query(ardu_id) -> str:
    return f'''mutation{{
        unloadPlantFromArdu(arduId: "{ardu_id}")
        {{ arduId }}
    }}
    '''