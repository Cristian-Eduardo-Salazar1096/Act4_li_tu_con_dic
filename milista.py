# Ejemplo de uso de listas

Misnovias=["Agripina", "Anastacia", "Maria"]
MisNumeros=[666,77,10]

# Mostrando mis Novias
print(Misnovias)

# Mostrando mis Numeros 
print(MisNumeros)

print("--------Accediendo a los elementos de la lista--------")

# Mostrando mis Novias (solo una en especifico)
print(Misnovias[1])

# Mostrando mis Novias (solo una en especifico de derecha a izquierda)
print(Misnovias[-1])

if "Ana" in Misnovias:
  print("Si, 'Ana' esta en la lista Misnovias")
else:
  print("Chale no eres mi novia")

print("Numero de novias")
NNovias=len(Misnovias)
print(f"Numero de novias: {NNovias}")

posicion=0
print("Ciclo for en listas")
for medianaranja in Misnovias:
  print(posicion,"", medianaranja)
  posicion = posicion + 1
