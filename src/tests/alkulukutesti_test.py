import unittest
import sympy
import Funktiot.alkulukutesti as subject_test
import Funktiot.alkulukugeneraattori as subject_generator
import Funktiot.matikkapalikat as math_help

class TestFirstPrimes(unittest.TestCase):
    def setUp(self):
        self.first_primes_attempt = subject_test._first_primes()
        self.first_primes_actual =[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31,
                                   37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 
                                   79, 83, 89, 97, 101, 103, 107, 109, 113,
                                   127, 131, 137, 139, 149, 151, 157, 163,
                                   167, 173, 179, 181, 191, 193, 197, 199,
                                   211, 223, 227, 229, 233, 239, 241, 251,
                                   257, 263, 269, 271, 277, 281, 283, 293,
                                   307, 311, 313, 317, 331, 337, 347, 349,
                                   353, 359, 367, 373, 379, 383, 389, 397,
                                   401, 409, 419, 421, 431, 433, 439, 443,
                                   449, 457, 461, 463, 467, 479, 487, 491,
                                   499, 503, 509, 521, 523, 541, 547, 557,
                                   563, 569, 571, 577, 587, 593, 599, 601,
                                   607, 613, 617, 619, 631, 641, 643, 647,
                                   653, 659, 661, 673, 677, 683, 691, 701,
                                   709, 719, 727, 733, 739, 743, 751, 757,
                                   761, 769, 773, 787, 797, 809, 811, 821,
                                   823, 827, 829, 839, 853, 857, 859, 863,
                                   877, 881, 883, 887, 907, 911, 919, 929,
                                   937, 941, 947, 953, 967, 971, 977, 983,
                                   991, 997]
    
    def test_content(self):
        self.assertEqual(self.first_primes_attempt, self.first_primes_actual)

class TestFactorOut(unittest.TestCase):
    def test_odd(self):
        self.assertEqual(math_help._factor_out(20001),(0,20001))

    def test_even(self):
        self.assertEqual(math_help._factor_out(20000),(5,625))

class TestProbablePrimeTest(unittest.TestCase):
    def setUp(self):
        self.first_primes =subject_test._first_primes()
    
    def test_divisible_by_small_prime(self):
        self.assertEqual(subject_test._probable_prime_test(292681,40,self.first_primes),False)

class TestPrimeGeneration(unittest.TestCase):
    def setUp(self):
        self.first_primes = subject_test._first_primes()
    
    def test_primes(self):
        primes_to_check = []
        results = []
        for _ in range(40):
            primes_to_check.append(subject_generator._generate_probable_prime(1024,40))
        for i in primes_to_check:
            results.append(sympy.isprime(i))
        self.assertGreaterEqual(results.count(True),38)