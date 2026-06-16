from collections import deque

# Cola de personajes: (nombre_personaje, nombre_superheroe, genero)
cola = deque([
    ("Tony Stark", "Iron Man", "M"),
    ("Steve Rogers", "Capitán América", "M"),
    ("Natasha Romanoff", "Black Widow", "F"),
    ("Carol Danvers", "Capitana Marvel", "F"),
    ("Scott Lang", "Ant-Man", "M"),
    ("Wanda Maximoff", "Scarlet Witch", "F"),
    ("Sam Wilson", "Falcon", "M"),
    ("Stephen Strange", "Doctor Strange", "M"),
    ("Shuri", "Shuri", "F"),
])

# a. Nombre del personaje de la superhéroe Capitana Marvel
for personaje, heroe, genero in cola:
    if heroe.lower() == "capitana marvel":
        print("a) El personaje de Capitana Marvel es:", personaje)

# b. Superhéroes femeninos
print("\nb) Superhéroes femeninos:")
for personaje, heroe, genero in cola:
    if genero == "F":
        print("-", heroe)

# c. Personajes masculinos
print("\nc) Personajes masculinos:")
for personaje, heroe, genero in cola:
    if genero == "M":
        print("-", personaje)

# d. Nombre del superhéroe del personaje Scott Lang
for personaje, heroe, genero in cola:
    if personaje.lower() == "scott lang":
        print("\nd) El superhéroe de Scott Lang es:", heroe)

# e. Datos de los que comienzan con 'S'
print("\ne) Personajes o superhéroes que comienzan con 'S':")
for personaje, heroe, genero in cola:
    if personaje.startswith("S") or heroe.startswith("S"):
        print(f"- Personaje: {personaje}, Superhéroe: {heroe}, Género: {genero}")

# f. Verificar si Carol Danvers está en la cola
for personaje, heroe, genero in cola:
    if personaje.lower() == "carol danvers":
        print(f"\nf) Carol Danvers está en la cola y su superhéroe es: {heroe