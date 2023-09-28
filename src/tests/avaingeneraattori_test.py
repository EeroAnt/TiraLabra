import unittest
import Funktiot.avaingeneraattori as subject

class TestFunctions(unittest.TestCase):
    def test_gcd(self):
        return self.assertEqual(subject.gcd(1071,462),21)
    
    def test_lcm(self):
        return self.assertEqual(subject.lcm(1071,462),23562)