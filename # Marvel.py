# Lista de personajes MCU con nombre y año de primera aparición
personajes = [
    {"nombre": "Iron Man", "anio": 2008},
    {"nombre": "Black Widow", "anio": 2010},
    {"nombre": "Thor", "anio": 2011},
    {"nombre": "Hulk", "anio": 2008},
    {"nombre": "Captain America", "anio": 2011},
    {"nombre": "Rocket Raccoon", "anio": 2014},
    {"nombre": "Doctor Strange", "anio": 2016},
    {"nombre": "Thanos", "anio": 2012},
    {"nombre": "Spider-Man", "anio": 2016},
    {"nombre": "Black Panther", "anio": 2016}
]

# a. Listado ascendente por nombre
print("a) Personajes ordenados por nombre:")
for p in sorted(personajes, key=lambda x: x["nombre"]):
    print(f"- {p['nombre']} ({p['anio']})")

# b. Primer y último personaje en aparecer (sin recorrer toda la lista)
anios = [p["anio"] for p in personajes]
anio_min = min(anios)
anio_max = max(anios)

primeros = [p["nombre"] for p in personajes if p["anio"] == anio_min]
ultimos = [p["nombre"] for p in personajes if p["anio"] == anio_max]

print("\nb) Primeros en aparecer:", primeros, "en", anio_min)
print("   Últimos en aparecer:", ultimos, "en", anio_max)

# c. Listado descendente por año
print("\nc) Personajes ordenados por año (descendente):")
for p in sorted(personajes, key=lambda x: x["anio"], reverse=True):
    print(f"- {p['nombre']} ({p['anio']})")

# d. Rango de años
rango = anio_max - anio_min
print(f"\nd) Rango de años entre el primero y el último: {rango} años")

# e. Verificar Capitan America y Rocket Raccoon
buscados = ["Captain America", "Rocket Raccoon"]
print("\ne) Búsqueda de personajes:")
for nombre in buscados:
    encontrado = next((p for p in personajes if p["nombre"].lower() == nombre.lower()), None)
    if encontrado:
        print(f"- {nombre} apareció en {encontrado['anio']}")
    else:
        print(f"- {nombre} no está en la lista")
