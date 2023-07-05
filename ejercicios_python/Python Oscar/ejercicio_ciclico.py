#Ejercicio 1 Vendedores
"""opw="si"
while opw=="si":
    num_vendedores=int(input("Ingrese el número de vendedores: "))
    for op in range(num_vendedores):
        sueldo_base=float(input(f"Digite el sueldo base del vendedor {op+1}: "))
        venta_1=float(input("Ingrese el valor de la venta 1: "))
        comision_1=venta_1*0.1
        print(f"Comisión de su venta 1: {venta_1*0.1}")
        venta_2=float(input("Ingrese el valor de la venta 2: "))
        comision_2=venta_2*0.1
        print(f"Comisión de su venta 2: {venta_2*0.1}")
        venta_3=float(input("Ingrese el valor de la venta 3: "))
        comision_3=venta_3*0.1
        print(f"Comisión de su venta 3: {venta_3*0.1}")
        comision=comision_1+comision_2+comision_3
        total=sueldo_base+comision
        print(f"El vendedor tuvo en total de comision de las 3 ventas {comision} más su sueldo base {sueldo_base}, un total de sueldo de: {total}")
    opw=input("Quiere usar el programa de nuevo? escriba si o no: ")"""
    
#Ejercicio 2 bolas de descuento
"""op="si"
while op=="si":
    boli_roja=0.45
    boli_amarilla=0.25
    total_compra=int(input("Digite el total de la compra: "))
    decision=input("Elige el color de la bola para ganarte premios, elige entre roja, amarilla y blanca (Escribir el color en minusculas): ")
    if decision=="roja":
        descuento=total_compra*boli_roja   
        print(f"Al elegir la bola roja, se ganó un 45% de descuento. Su compra fue de {total_compra} y su decuento de {descuento}, en total debe pagar {total_compra-descuento}")
    elif decision=="amarilla":
        descuento=total_compra*boli_amarilla
        print(f"Al elegir la bola amarilla, se ganó un 25% de descuento. Su compra fue de {total_compra} y su decuento de {descuento}, en total debe pagar {total_compra-descuento}")
    elif decision=="blanca":
        print(f"Al elegir la bola blanca, no se ganó ningún descuento. Su compra fue de {total_compra}")
    else:
        print(f"Lo siento, tu respuesta no se puedo entender")
    op=input("Quiere usar el programa de nuevo? escriba si o no: ")"""

#Ejercicio 3 Materia profesor
"""alumnos_desapro=0
alumnos_apro=0
for i in range(40):
    print(f"Alumno {i+1}")
    calificacion_1=float(input("Ingrese el valor de la calificación 1 recuerde que es de 1 a 5: "))
    calificacion_2=float(input("Ingrese el valor de la calificación 2 recuerde que es de 1 a 5: "))
    calificacion_3=float(input("Ingrese el valor de la calificación 3 recuerde que es de 1 a 5: "))
    calificacion_4=float(input("Ingrese el valor de la calificación 4 recuerde que es de 1 a 5: "))
    calificacion_5=float(input("Ingrese el valor de la calificación 5 recuerde que es de 1 a 5: "))
    promedio=(calificacion_1+calificacion_2+calificacion_3+calificacion_4+calificacion_5)/5
    if promedio>=3:
        alumnos_apro+=1
        print(f"El alumno aprobó su promedio fue de {promedio}, tiene derecho a examén de nivelación")
    else:
        alumnos_desapro+=1
        print(f"El alumno desaprobó su promedio fue {promedio}, no tiene derecho a examén de nivelación")
print(f"El total de los alumnos aprobados es {alumnos_apro} y el total de alumnos desaprobados es {alumnos_desapro}")"""

#Ejercicio 4 votos
"""candidato_1=0
candidato_2=0
candidato_3=0
for i in range(2500000):
    print(f"Numero de voto {i+1}")
    votos=int(input("Hay 3 candidatos para votar, elija por cuál quiere votar de los tres, escriba 1, 2 o 3 "))
    if votos==1:
        candidato_1+=1
        print("Has votado correctamente por el candidato 1")
    elif votos==2:
        candidato_2+=1
        print("Has votado correctamente por el candidato 2")
    elif votos==3:
        candidato_3+=1
        print("Has votado correctamente por el candidato 3")
    else:
        print("No has votado correctamente, vuelve a intentarlo")
        
if candidato_1>candidato_2 and candidato_1>candidato_3:
    print(f"Él ganador es el candidato 1, su número de votos fue {candidato_1}")
elif candidato_2>candidato_1 and candidato_2>candidato_3:
    print(f"Él ganador es el candidato 2, su número de votos fue {candidato_2}")
elif candidato_3>candidato_1 and candidato_3>candidato_2:
    print(f"Él ganador es el candidato 3, su número de votos fue {candidato_3}")
elif candidato_1==candidato_2 and candidato_1!=candidato_3:
    print(f"El candidato 1 y candidato 2 tuvieron los mismos votos {candidato_1}")
elif candidato_1==candidato_3 and candidato_1!=candidato_2:
    print(f"El candidato 1 y candidato 3 tuvieron los mismos votos {candidato_1}")
elif candidato_2==candidato_3 and candidato_2!=candidato_1:
    print(f"El candidato 2 y candidato 3 tuvieron los mismos votos {candidato_2}")
else:
    print(f"Los votos fueron iguales para cada uno, cada candidato tiene {candidato_1} votos")"""


#Ejercicio 5 examén física
"""alumno_49=0
alumno_50_69=0
alumno_70_79=0
alumno_80=0
for i in range(100):
    print(f"Numero de alumno {i+1}")
    calificacion=int(input("Ingresar el valor de la calificación (recuerde que es de 1 a 100): "))
    if calificacion<50:
        alumno_49+=1
        print("Él alumno sacó menos que 50")
    elif calificacion>=50 and calificacion<70:
        alumno_50_69+=1
        print("Él alumno sacó 50 o más pero menos de 70")
    elif calificacion>=70 and calificacion<80:
        alumno_70_79+=1
        print("El alumno sacó 70 o más pero menos que 80")
    else:
        alumno_80+=1
        print("Él alumno sacó 80 o más")
        
print(f"Él número de alumnos que sacaron menos de 50 son {alumno_49}")
print(f"Él número de alumnos que sacaron 50 o más pero menos de 70 son {alumno_50_69}")
print(f"Él número de alumnos que sacaron 70 o más pero menos de 80 son {alumno_70_79}")
print(f"Él número de alumnos que sacaron más de 80 son {alumno_80}")"""