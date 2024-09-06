arcoiris = ("Azul", "Verde", "Rojo", "Amarillo")

print(arcoiris)
print("---Longitud Arcoiris---")
print(len(arcoiris))

animales = ("Pantera", 20, "Estatura", 1.7)

print(animales)
print("Elementos de la tupla")
print(animales[2])

rateros = ("Juan", "Ana", "Pedro")
y = list(rateros)
y[0] = "kiwi"
x = tuple(y)

print(x)
Nanimal=("boby","chestos")
y = list(Nanimal)
print(y)
y.append("tontolin")
otratupla = tuple(y)

print(otratupla)
print("Uso de for en tuplas")

for elcolor in arcoiris:
    print(elcolor)