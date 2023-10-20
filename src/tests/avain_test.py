import unittest
import Funktiot.avaingeneraattori as keygenerator
import Funktiot.avaintallennus as keysaver

class TestEncryption(unittest.TestCase):
    def setUp(self):
        (n,e,d) = keygenerator._generate_key()
        keysaver._save_key("Test_A",n,e,d)
    
    def test_key_found(self):
        key = keysaver._get_key("Test_A_public")
        return self.assertEqual(tuple,type(key))
    
    def test_key_not_found(self):
        key = keysaver._get_key("Test_not_found_i_hope")
        return self.assertEqual(None,key)