import unittest
import Funktiot.avaingeneraattori as subject

class TestFunctions(unittest.TestCase):
    def test_gcd(self):
        return self.assertEqual(subject._gcd(1071,462),21)
    
    def test_lcm(self):
        return self.assertEqual(subject._lcm(1071,462),23562)
    
    def test_eucleidian_div_quotient(self):
        return self.assertEqual(subject._quotient_from_eucleidian_div(244,5),48)
    
    def test_extended_gcd(self):
        return self.assertEqual(subject._extended_gcd(240,46),47)