print("Promedio de calificaciones (Num negativo para salir)")
calif = 1
tc=0
prom=0
while calif >0:
    calif = int(input("Escribe una calificacion : "))
    if calif > 0:
        prom=prom+calif
        tc+=1
    
print("Terminaste el ciclo.")
print("El total de calificaciones que ingresaste es.." ,tc)
print("El promedio es...", prom/tc)
