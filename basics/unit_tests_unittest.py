import unittest

def sum_two_numbers(a, b):
    return a + b

class SumTest(unittest.TestCase):

    def testCalculation(self):
        self.assertEqual(sum_two_numbers(1,1), 2)
        self.assertEqual(sum_two_numbers(2,2), 4)
        self.assertTrue(sum_two_numbers(2,2) == 4)
        self.assertGreater(sum_two_numbers(2,2), 3)
        self.assertLess(sum_two_numbers(2,2), 5)


    def testFalseCalculation(self):
        self.assertFalse(sum_two_numbers(2,2) == 5)

    def setUp(self):
        self.test_elements = ( (2,4), (3,6), (4,8) )
        #print("setUp executed")

    def testCalculationWithSetupValues(self):
        for (i,res) in self.test_elements:
            self.assertEqual(sum_two_numbers(i,i),res)

    def tearDown(self):
        self.test_elements = None
        #print("tearDown executed")


if __name__ == "__main__":
    unittest.main()
