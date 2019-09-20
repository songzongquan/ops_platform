import unittest

class MyTest(unittest.TestCase):
    def tearDown(self):
        print('111')
    def setUp(self):
        print('2222')

    @classmethod
    def tearDownClass(self):
        print('44444')

    @classmethod
    def setUpClass(self):
        print('333333')

    def test_a_run(self):
        self.assertEqual(1,1)

    def test_b_run(self):
        self.assertEqual(2,2)

if __name__ == '__main__':
    unittest.main()

