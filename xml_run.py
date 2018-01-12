import unittest
from unittest import TestSuite


import xmlrunner

from tests import dog_tests

if __name__ == '__main__':
    suite = TestSuite()
    suite.addTest(dog_tests("test_01_dog_paws"))
    suite.addTest(dog_tests("test_02_dog_wag_tail"))
    suite.addTest(dog_tests("test_03_dog_body"))

    testRunner = xmlrunner.XMLTestRunner(output='test-reports', verbosity=2)

    testRunner.run(suite)
