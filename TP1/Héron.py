#Exercice 3 Mascaro Matteo
def heron_square_root(q, n, x1):
    x_n = x1
    for i in range(n):
        x_n = 0.5 * (x_n + q/x_n)
        print("Approximation de l'itération" , i+1, ":", x_n)
    return x_n

q = int(input("Entrez le nombre q : "))
x1 = int(input("Entrez la valeur de départ x1 : "))
n = int(input("Entrez le nombre d'itérations n : "))
result = heron_square_root(q, n, x1)
print("La racine carrée de", q, "est approximativement :", result)
