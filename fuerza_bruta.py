from string import ascii letters, digits from itertools import product
caracteres = ascii_letters+digits
def buscador (con):
archivo = open("combinaciones.txt", "w")
if 10 <= len(con) <= 14: for i in range(3, 5): for comb in product (caracteres, repeat=l): prueba ="".join(comb)
archivo.write(pruebat"In") if prueba = con: print("Tu contrseña es >".format (prueba)) archivo.close() break
else:
print("Ingresa una contraseña de longitud entre 10 y 14 caracteres")