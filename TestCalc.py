import unittest
import logging
import sys
from Calculator import Calculator
from BasicArithmitic import *
from ReaderOfCSVs import ReaderOfCSVs


logger = logging.getLogger()
logger.level = logging.DEBUG
stream_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stream_handler)
pathAddition = r'src/UnitTestAddition.csv'
pathSubtraction = r'src/UnitTestSubtraction.csv'
pathDivision = r'src/UnitTestDivision.csv'
pathMultiplication = r'src/UnitTestMultiplication.csv'


class MyTestCase(unittest.TestCase):

    #calcu = Calculator()
    def setUp(self):
        stream_handler.stream = sys.stdout
        self.calc = Calculator()

    # def test_something(self):
    #     self.assertEqual(True, True)
    #
    # def test_instantiate_calculator(self):
    #     # calc = Calculator()
    #     self.assertIsInstance(self.calc, Calculator)
    #     print(self.calc.count)
    #
    # def test_addition(self):
    #     #calc = Calculator()
    #     self.assertEqual(self.calc.add(2,2), 4)
    #     print(self.calc.count)
    #
    # def test_subtraction(self):
    #     #calc = Calculator()
    #     self.assertEqual(self.calc.sub(2,2), 0)
    #     print(self.calc.count)
    #
    # def test_multiplication(self):
    #     #calc = Calculator()
    #     self.assertEqual(self.calc.mul(2,2), 4)
    #
    # def test_division(self):
    #     #calc = Calculator()
    #     self.assertEqual(self.calc.div(2,2), 1)
    #
    # def test_square(self):
    #     #calc = Calculator()
    #     self.assertEqual(self.calc.square(2), 4)
    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calc, Calculator)

    def test_addition(self):
        print("\nin Addition!\n")
        self.csvReaderAdd = ReaderOfCSVs(pathAddition)
        addition = self.csvReaderAdd.create_class_dynamically("addition")
        for add in addition:
            #print(add.__name__, "\t", add.__dict__['Value 1'], "\t", add.__dict__['Value 2'], "\t", add.__dict__['Result'])
            self.assertEqual(self.calc.add(int(add.__dict__['Value 1']), int(add.__dict__['Value 2'])), int(add.__dict__['Result']))

    def test_subtraction(self):
        print("\nin sub\n")
        self.csvReaderAdd = ReaderOfCSVs(pathSubtraction)
        subsub = self.csvReaderAdd.create_class_dynamically("sub")
        for sub in subsub:
            #print(sub.__name__, "\t", sub.__dict__['Value 1'], "\t", sub.__dict__['Value 2'], "\t", sub.__dict__['Result'])
            self.assertEqual(self.calc.sub(int(sub.__dict__['Value 2']), int(sub.__dict__['Value 1'])), int(sub.__dict__['Result']))

    def test_divide(self):
        print("\nin divdidididididid\n")
        self.csvReaderDiv = ReaderOfCSVs(pathDivision)
        divdiv = self.csvReaderDiv.create_class_dynamically("divdiv")
        for div in divdiv:
            #print(div.__name__, "\t", div.__dict__['Value 1'], "\t", div.__dict__['Value 2'], "\t", div.__dict__['Result'])
            self.assertAlmostEqual(self.calc.div(int(div.__dict__['Value 2']), int(div.__dict__['Value 1'])), float(div.__dict__['Result']))

    def test_multiply(self):
        print("\nmulti-multi\n")
        self.csvReaderMulti = ReaderOfCSVs(pathMultiplication)
        multiMulti = self.csvReaderMulti.create_class_dynamically("multimulti")
        for multi in multiMulti:
            self.assertEqual(self.calc.mul(int(multi.__dict__['Value 1']), int(multi.__dict__['Value 2'])), int(multi.__dict__['Result']))

    def test_squareRootFromBasicArithmitic(self):
        self.assertEqual(squareRoot(16), 4)
        self.assertEqual(squareRoot(4), 2)


if __name__ == '__main__':
    unittest.main()
