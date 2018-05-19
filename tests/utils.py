def generatorTester(generatorToTest, expectedValues):

    for generatorValue, expectedValue in zip(generatorToTest, expectedValues):
        assert generatorValue == expectedValue, 'Value diff'
