import unittest
import Funktiot.salaus as subject
import Funktiot.avaingeneraattori as keygenerator
import Funktiot.avaintallennus as keysaver

class TestEncryption(unittest.TestCase):
    def setUp(self):
        (n,e,d) = keygenerator._generate_key()
        keysaver._save_key("Test_A",n,e,d)
        (n,e,d) = keygenerator._generate_key()
        keysaver._save_key("Test_B",n,e,d)
    
    def test_decryption_right_key(self):
        public_key = keysaver._get_key("Test_A_public")
        subject._encrypt("Testiviesti",public_key,"Test")
        private_key = keysaver._get_key("Test_A_private")
        self.assertEqual(subject._decrypt("Test",private_key),"Testiviesti")
    
    def test_decryption_wrong_key(self):
        public_key = keysaver._get_key("Test_B_public")
        subject._encrypt("Testiviesti",public_key,"Test")
        private_key = keysaver._get_key("Test_A_private")
        self.assertEqual(subject._decrypt("Test",private_key),"Avain ei ollut yhteensopiva")
    
    def test_decryption_file_not_found(self):
        private_key = keysaver._get_key("Test_A_private")
        self.assertEqual(subject._decrypt("Toivottavasti_taman_nimista_tiedostoa_ei_ole",private_key),"Tiedostoa ei löytynyt")
    