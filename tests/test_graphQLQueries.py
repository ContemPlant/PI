import unittest

from src.backendConnect.graphQLQueries import \
    add_sensor_data_queryfn, \
    subscribe_to_ardu_change_query


class TestGraphQLQueries(unittest.TestCase):

    def test_add_sensor_data_queryfn(self):
        expected = \
            "mutation{{"\
                "addSensorDates("\
                    "input: {{"\
                      "temperatureValue: 32.93"\
                      "humidityValue: 1293"\
                      "radiationValue: 1832"\
                      "loudnessValue: 429"\
                      'timeStamp: "123094832"'\
                      'arduId:"1329"'\
                "}}) {{ id }}"\
            "}}"
        

        assert expected == add_sensor_data_queryfn(32.93, 1293, 1832, \
                                                    429, 123094832, 1329)

    def test_subscribe_to_ardu_change_query(self):
        #TODO
        assert True


if __name__ == '__main__':
    unittest.main()
