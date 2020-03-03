import random

numeros = []

for i in range(1000):
    numeros.append(random.randint(0, 1000))

print(numeros)
numeros.sort(reverse=True)
print(numeros)
