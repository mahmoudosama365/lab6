
import unittest
from calculator import Calc  

class TestCalculator(unittest.TestCase):
    def test_add(self):
        result = Calc.add(5, 10)
        self.assertEqual(result, 15)

if __name__ == '__main__':
    unittest.main()  
