import math

def celsius_to_fahrenheit(temp):
    return (float(temp) *(5 / 9)) - 32
def fahrenheit_to_celsius(temp):
    return (float(temp) *(9 / 5)) + 32

print('Welcome to the temperature converter, please enter "C" if you want to convert Celsius to Fahrenheit or "F" for the opposite:')
choice = input("->").lower()
if choice == "c":
    temp = input("Rentrez la température en Celsius : ")
    resultat = celsius_to_fahrenheit(temp)
    print("La température est de" + str(resultat) + "degrés Fahrenheit")
else :
    temp = input("Rentrez la température en Fahrenheit : ")
    fahrenheit_to_celsius(temp)
    resultat = celsius_to_fahrenheit(temp)
    print("La température est de " + str(resultat) + " degrés Celsius")

