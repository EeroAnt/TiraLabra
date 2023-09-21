import Funktiot.alkulukutesti as primalitytest
import Funktiot.alkulukugeneraattori as generator
import time


def UI():
    while True:
        print("Mitä tehdään?")
        options = {1 : "Tuota n-bittinen alkuluku",
                0 : "Lopeta"}
        for key, value in options.items():
            print(key, ":", value)
        choise = int(input())
        if choise == 1:
            bits = int(input("Montako bittiä? "))
            attempts = int(input("Monta kertaa haastetaan? "))
            start = time.time()
            print(generator.generate_probable_prime(bits,attempts))
            end = time.time()
            print(f"Aikaa kului {end-start}s.")
        if choise == 0:
            break