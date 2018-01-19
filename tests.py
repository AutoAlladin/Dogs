import unittest
from Dogs import Dog


class dog_tests(unittest.TestCase):
    dog = None

    def setUp(self):
        self.dog = Dog()


    def test_01_dog_paws(self):
        with self.subTest("run_test"):
            if len(self.dog.paws)== 4:
                print("It's a normal dog")
            elif len(self.dog.paws)> 4:
                print("It's not a dog - it is monster !!! ")
            elif len(self.dog.paws)< 4:
                print("It's a broken dog")



        with self.subTest('left'):
            self.assertEqual(True, True)
        with self.subTest('right'):
            self.assertEqual(True, True)

    # try:

    #     if len(self.dog.paws) == 4:
    #         self.assertFalse(True, 'Everything is great')
    #
    # except Exception as e:
    #         self.assertTrue(False, 'ERROR' + e.__str__())


    def test_02_dog_wag_tail(self):
        self.dog.start_wag_tail()
        if self.dog.tail == "|_|" :
            print("Dog is happy")
        else:
            print("Dog is sad")

    def test_03_dog_body(self):
        if self.dog.body == self.dog.wool :
            print(self.dog.wool)


    # def test_s(self):
    #     with self.subTest('left'):
    #         self.assertEqual(True, True)
    #     with self.subTest('right'):
    #         self.assertEqual(True, True)

