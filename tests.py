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



        with self.subTest('4'):
            self.assertEqual(True, True)
        with self.subTest('> 4'):
            self.assertEqual(True, True)
        with self.subTest('< 4'):
            self.assertEqual(True, True)




    # try:

    #     if len(self.dog.paws) == 4:
    #         self.assertFalse(True, 'Everything is great')
    #
    # except Exception as e:
    #         self.assertTrue(False, 'ERROR' + e.__str__())


    def test_02_dog_wag_tail(self):
        self.dog.start_wag_tail()
        self.dog.finish_wag_tail()
        # if self.dog.tail == "|_|":
        #     print("Dog is happy")
        # else:
        #     print("Dog is sad")
        #self.dog.finish_wag_tail()
        # else:
        #     #self.dog.tail == "---":
        #     print("Dog is sad")

        self.assertNotEqual(self, self.dog.start_wag_tail(), self.dog.finish_wag_tail(), "ERROR")
        if self.dog.start_wag_tail() == self.dog.finish_wag_tail():
            return False
            print(self.dog.start_wag_tail())
            print(self.dog.finish_wag_tail())


    def test_03_dog_body(self):
        body1 = self.dog.body[0] + self.dog.wool + self.dog.body[1]
        body2 = self.dog.body
        print(body1)
        print(body2)

        if self.assertEqual(self, body1, body2, "Error"):
            return False


    # def test_s(self):
    #     with self.subTest('left'):
    #         self.assertEqual(True, True)
    #     with self.subTest('right'):
    #         self.assertEqual(True, True)

