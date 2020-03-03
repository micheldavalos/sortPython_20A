from random import randint

class Automovil:
    def __init__(self):
        self.placas = ""
        self.modelo = 0
        self.marca = ""
        self.km = 0

    def __str__(self):
        return "{0:6} {1:4} {2:6} {3:4}".format(self.placas, self.modelo, self.marca, self.km)

    def __lt__(self, other):
        return self.modelo < other.modelo

marcas = ["VW", "BMW", "Audi", "Fiat", "Nissan", "Honda", "Mazda"]
placas = ["ABC", "JVC", "JZM", "MDB", "UDG"]

autos = []

for i in range(100):
    a = Automovil()
    a.placas = placas[randint(0, len(placas)-1)] \
               + str(randint(100, 999))
    a.modelo = randint(2000, 2020)
    a.marca = marcas[randint(0, len(marcas)-1)]
    a.km = randint(0, 1000)
    autos.append(a)

for auto in autos:
    print(auto)

#autos.sort()
def sort_by_km(auto):
    return auto.km
#autos.sort(key=sort_by_km)
autos.sort(key=lambda auto: auto.marca)
print("\n\nOrdenados:")
for auto in autos:
    print(auto)
