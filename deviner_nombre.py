import random

def deviner_nombre():
    nombre_a_deviner = random.randint(1, 100)
    essais = 0
    print("Devine le nombre entre 1 et 100 !")

    while True:
        essai = int(input("Ton essai : "))
        essais += 1
        if essai < nombre_a_deviner:
            print("Trop petit !")
        elif essai > nombre_a_deviner:
            print("Trop grand !")
        else:
            print(f"Bravo ! Tu as trouvé en {essais} essais.")
            break

deviner_nombre()
