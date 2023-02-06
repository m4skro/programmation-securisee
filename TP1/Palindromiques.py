#Exercice 2 Mascaro Matteo
import math
limit = 100
limit = str(limit)

print('Welcome palindromiques numbers put any multipliation with 2 numbers in each side :')
print("Rentrez la multiplication ex : (91 * 99) ")
A = input("Rentrez la valeur A = ")
B = input("Rentrez la valeur B = ")

"""
print(A)
J'arrive pas à faire une boucle erreur ( à voir plus tard)
print(B)
"""

var = int(A) * int(B)
print(var)
var = str(var)
if(var == var[::-1]):
      print("L'entrée est un palindrome")
else:
      print("L'entrée n'est pas un palindrome")