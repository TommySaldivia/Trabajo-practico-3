from collections import deque

# Cola de notificaciones: (hora, aplicación, mensaje)
notificaciones = deque([
    ("10:15", "Facebook", "Nuevo comentario en tu publicación"),
    ("11:50", "Twitter", "Aprendiendo Python con ejemplos"),
    ("12:30", "Instagram", "Nueva historia de tu amigo"),
    ("14:10", "Twitter", "Python es genial para análisis de datos"),
    ("15:00", "Facebook", "Nueva solicitud de amistad"),
    ("16:20", "WhatsApp", "Grupo de estudio: reunión mañana"),
    ("15:45", "Twitter", "Hoy no hablamos de Java"),
])

# a) Eliminar todas las notificaciones de Facebook
def eliminar_facebook(cola):
    return deque([n for n in cola if n[1].lower() != "facebook"])

notificaciones = eliminar_facebook(notificaciones)
print("a) Cola sin notificaciones de Facebook:")
for n in notificaciones:
    print("-", n)

# b) Mostrar notificaciones de Twitter con 'Python' sin perder datos
print("\nb) Notificaciones de Twitter con 'Python':")
for hora, app, mensaje in notificaciones:
    if app.lower() == "twitter" and "python" in mensaje.lower():
        print("-", (hora, app, mensaje))

# c) Usar pila para notificaciones entre 11:43 y 15:57
def en_rango(hora, inicio, fin):
    # Convertir a minutos para comparar
    h, m = map(int, hora.split(":"))
    total = h * 60 + m
    hi, mi = map(int, inicio.split(":"))
    hf, mf = map(int, fin.split(":"))
    return (hi * 60 + mi) <= total <= (hf * 60 + mf)

pila = []
for n in notificaciones:
    if en_rango(n[0], "11:43", "15:57"):
        pila.append(n)

print(f"\nc) Cantidad de notificaciones entre 11:43 y 15:57: {len(pila)}")
print("   Notificaciones almacenadas en la pila:")
for n in pila:
    print("-", n)
