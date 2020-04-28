import unittest

from faker import Faker
from src.Example.Example import Example

class ExampleTest(unittest.TestCase):
    def setUp(self):
        self.faker = Faker()

    def testReturnConcatenatedProperties_returnsContructorArgumentsAsConcatenatedString(self):
        inputString = self.faker.word()
        inputNumber = self.faker.random_int()
        example = Example(inputString, inputNumber)

        result = example.returnConcatenatedProperties()

        self.assertEqual(result, f"{inputString} {inputNumber}")
