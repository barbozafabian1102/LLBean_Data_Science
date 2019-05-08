# promediar

pixel = [0.6,0.3,0.4]

suma = pixel[0]+pixel[1]+pixel[2]

n = len(pixel)

promedio = suma/n

print('suma=', suma, 'n=',promedio)

# otra solucion
# ciclos

p=0
for numero in pixel:
    p += numero

p = p/len(pixel)

print('el promedio es',p)

# tercer solucion

mi_suma = sum(pixel)
mi_promedio =  mi_suma/len(pixel)
print('la suma es',mi_suma,'el promedio es',mi_promedio)

# cuarta opcion

promedio4 =  sum(pixel)/len(pixel)

# practicando el if

if mi_promedio >= 0.5:
    print('El Pixel es blanco')
else:
    print('El Pixel es negro')


