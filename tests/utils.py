def generator_tester(generator_to_test, expected_values):

    for generatorValue, expectedValue in zip(generator_to_test, expected_values):
        if generatorValue != expectedValue:
            return False

    return True