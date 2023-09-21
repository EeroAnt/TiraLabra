import unittest
import Funktiot.alkulukutesti as subject

class TestFirstPrimes(unittest.TestCase):
    def setUp(self):
        self.first_primes_attempt = subject.first_primes()
        self.first_primes_actual =[3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
                                   41, 43, 47, 53, 59, 61, 67, 71, 73, 79,
                                   83, 89, 97, 101, 103, 107, 109, 113,
                                   127, 131, 137, 139, 149, 151, 157, 163,
                                   167, 173, 179, 181, 191, 193, 197, 199,
                                   211, 223, 227, 229, 233, 239, 241, 251,
                                   257, 263, 269, 271, 277, 281, 283, 293,
                                   307, 311, 313, 317, 331, 337, 347, 349,
                                   353, 359, 367, 373, 379, 383, 389, 397,
                                   401, 409, 419, 421, 431, 433, 439, 443,
                                   449, 457, 461, 463, 467, 479, 487, 491,
                                   499, 503, 509, 521, 523, 541, 547]
    def test_length(self):
        self.assertEqual(len(self.first_primes_attempt), 100)
    
    def test_content(self):
        self.assertEqual(self.first_primes_attempt, self.first_primes_actual)

class TestFactorOut(unittest.TestCase):
    def test_odd(self):
        self.assertEqual(subject.factor_out(20001),(0,20001))

    def test_even(self):
        self.assertEqual(subject.factor_out(20000),(5,625))

class TestProbablePrimeTest(unittest.TestCase):
    def setUp(self):
        self.first_primes =[3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
                            41, 43, 47, 53, 59, 61, 67, 71, 73, 79,
                            83, 89, 97, 101, 103, 107, 109, 113,
                            127, 131, 137, 139, 149, 151, 157, 163,
                            167, 173, 179, 181, 191, 193, 197, 199,
                            211, 223, 227, 229, 233, 239, 241, 251,
                            257, 263, 269, 271, 277, 281, 283, 293,
                            307, 311, 313, 317, 331, 337, 347, 349,
                            353, 359, 367, 373, 379, 383, 389, 397,
                            401, 409, 419, 421, 431, 433, 439, 443,
                            449, 457, 461, 463, 467, 479, 487, 491,
                            499, 503, 509, 521, 523, 541, 547]
    def test_even(self):
        self.assertEqual(subject.probable_prime_test(35000,40,self.first_primes),"Ei alkuluku, parillinen")
    
    def test_divisible_by_small_prime(self):
        self.assertEqual(subject.probable_prime_test(299209,40,self.first_primes),"Ei alkuluku, jaollinen pienellä alkuluvulla")
    
    def test_probable_prime(self):
        self.assertEqual(subject.probable_prime_test(912991,40,self.first_primes), "Luultavasti alkuluku")