# Random password generator 26/10 2020 17:37

import random
import string
import sys

users = {}

status = ""

confirmation = "Uporabniški račun ustvarjen."

def displayMenu():
    status = input("Ali ste registrirani uporabnik? da/ne? Ali pa vpišite 'konec' za ustavitev programa: ").upper()
    if status == "DA":
        oldUser()

    elif status == "NE":
        newUser()

def newUser():
    createLogin = input("Ustvarite vaše uporabniško ime: ")

    if createLogin in users:
        print("To uporabniško ime je že v rabi.")
    
    else:
        createPassw = input("Želite geslo ustvariti sami ali s pomočjo programa? ročno/auto? ").upper()
        if createPassw == "ROČNO":
            manual = input("Ustvarite geslo: ")
            users[createLogin] = manual
            print(confirmation)

        elif createPassw == "AUTO":

            toughness = int(input("Kako dolgo naj bo vaše geslo (npr. 9): "))
            
            special_char = ["!", '"', "#", "$", "%", "&", "/", "(", ")", "?", "*"]

            password = ""

            for number in range(toughness):
                decision = random.randint(0, 100)
                number == "sys"

                if decision >= 60:
                    part1 = random.choice(string.ascii_letters)
                    password += part1
                    
                elif decision < 40:
                    part2 = str(random.randint(0, 9))
                    password += part2

                elif decision >= 40 and decision < 60:
                    part3 = random.choice(special_char)
                    password += part3
            
            print("Vaše geslo je '" + password + "'.")
            users[createLogin] = password
            print(confirmation)

        else:
            print("Prišlo je do napake prosimo poskusite še enkrat.")

    
def oldUser():
    login = input("Vpišite vaše uporabniško ime: ")
    passw = input("Vpišite vaše geslo: ")

    if login in users and users[login] == passw:
        print("Vpis uspešen")

    else: 
        print("Uporabniško ime ali geslo ni pravilno oziroma ne obstaja.")

while status != "KONEC":
    displayMenu()
