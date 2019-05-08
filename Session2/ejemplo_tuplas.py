# ejemplo tuplas
# crear una tupla de 5 elementos de tipos diferentes

mi_tupla = (1,'a', 'mi texto',True)

# imprimir la tupla

print (mi_tupla)

# agregar mas elementos!

mi_tupla = mi_tupla + (8,'c')

print (mi_tupla)

mi_tupla += (0,'x')
print(mi_tupla)

# subtupla
# desde el segundo hasta el penúltimo
print(mi_tupla [1:-1])

# subtupla con saltos
# los elementos pares

print('los elementos pares',mi_tupla[::2])

# IMPORTANTE
# los elementos impares

print('los elementos impares',mi_tupla[1::2])