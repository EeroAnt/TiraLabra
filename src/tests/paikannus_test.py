import unittest
import Funktiot.paikannus as subject_test
import Funktiot.avaingeneraattori as keygenerator
import Funktiot.avaintallennus as keysaver
import Funktiot.salaus as encryptor

class TestEncryption(unittest.TestCase):
    def setUp(self):
        (n,e,d) = keygenerator._generate_key()
        keysaver._save_key("Test_A",n,e,d)
        encryptor._encrypt("Testing",(n,e),"Testiest_message")

    def test_key_found(self):
        return self.assertEqual(subject_test._locate_key("Test_A"),True)
    
    def test_key_not_found(self):
        return self.assertEqual(subject_test._locate_key("Hopefully_not_found_Test"),False)
    
    def test_message_found(self):
        return self.assertEqual(subject_test._locate_message("Testiest_message"),True)
    
    def test_message_not_found(self):
        return self.assertEqual(subject_test._locate_message("Messiest_testage"),False)
    
