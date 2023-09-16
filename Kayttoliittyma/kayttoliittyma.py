import Funktiot.alkulukutesti as primalitytest
import Funktiot.alkulukugeneraattori as generator


def UI():
    while True:
        print("Mitä tehdään?")
        options = {1 : "Testaa alkuluku",
                2 : "Jaa kahden potenssit",
                3 : "Tuota n-bittinen alkuluku",
                0 : "Lopeta"}
        for key, value in options.items():
            print(key, ":", value)
        choise = int(input())
        if choise == 1:
            target = int(input("Mitä lukua testataan? "))
            attempts = int(input("Monta kertaa haastetaan? "))
            print(primalitytest.probable_prime_test(target,attempts))
        if choise == 2:
            target = int(input("Mitä lukua tutkitaan? "))
            print(primalitytest.factor_out(target))
        if choise == 3:
            bits = int(input("Montako bittiä? "))
            attempts = int(input("Monta kertaa haastetaan? "))
            print(generator.generate_probable_prime(bits,attempts))
        if choise == 0:
            break