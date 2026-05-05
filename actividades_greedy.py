actividades = [
    ("A", 1, 4),
    ("B", 1, 4),
    ("C", 1, 4),
    ("D", 1, 4),
    ("E", 1, 4),
    ("F", 1, 4),
]

actividades.sort(key = lambda x:x[2])
seleccionadas = []
fin_actual = 0

for activ idadces in actividades:
    nombre, inicio, fin = actividades
    if inicio >= fin_actual:
        seleccionadas.append(nombre)
        fin_actual = fin
print("actividades seleccionadas", seleccionadas)
