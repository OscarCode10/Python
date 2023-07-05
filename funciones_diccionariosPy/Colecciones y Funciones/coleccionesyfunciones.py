#Ejercicio 1 Pasajeros y Ciudades
"""passengers=[("Manuel Juárez", 19823451, "Armenia"),
              ("Gloria Galvis", 45789234, "Cali"),
              ("Rosa Ortiz", 45456234, "Medellín"),
              ("Eduardo Carrasquilla", 79844677, "Cali")]

cities=[("Armenia", "Quindío"),
          ("Cali", "Valle"),
          ("Medellín", "Antioquia")]

def createPass():
    nombre=input("Ingresa nombre completo: ")
    doc=int(input("Ingresa tu número de documento: "))
    city=input("Ingresa la ciudad a la que viajarás: ")
    passengers.append((nombre, doc, city))
    print(f"Se creó el pasajero {passengers}")

def createCity():
    city=input("Nombre de la ciudad: ")
    department=input("Nombre del departamento de la ciudad: ")
    cities.append((city, department))
    print(f"Se creó la ciudad {cities}")

def findCity():
    doc=int(input("Ingresa el número de documento por el que quieres buscar: "))
    for passenger in passengers:
        if passenger[1]==doc:
            return passenger[2]
    return "No se encontró la ciudad para ese documento"

def cantCity():
    city=input("Ingresa la ciudad: ")
    cant=0
    for passenger in passengers:
        if passenger[2]==city:
            cant+=1
    return f"Cantidad de pasajeros que viajan a {city}: {cant}"

def findDepart():
    doc=int(input("Ingresa el número de documento por el que quieres buscar: "))
    for passenger in passengers:
        if passenger[1]==doc:
            city=passenger[2]
            for c in cities:
                if c[0]==city:
                    return c[1]
    return "No se encontró el departamento para ese documento"

def cantDepart():
    dep=input("Ingresa el departamento: ")
    cant=0
    for passenger in passengers:
        city=passenger[2]
        for c in cities:
            if c[0]==city and c[1]==dep:
                cant+=1
                break
    return f"Cantidad de pasajeros que viajan a {dep}: {cant}"

op = "si"
while op == "si":
    print("1. Agregar pasajeros")
    print("2. Agregar ciudades")
    print("3. Buscar ciudad destino por la identificación")
    print("4. Cantidad de pasajeros que viajan a una ciudad")
    print("5. Buscar país destino mediante la identificación")
    print("6. Cantidad de pasajeros que viajan a un departamento")
    print("7. Salir del programa")
    decision = int(input("Ingresa qué operación quieres hacer: "))

    if decision == 1:
        print("Agregar pasajeros")
        createPass()
    elif decision == 2:
        print("Agregar ciudad")
        createCity()
    elif decision == 3:
        print("Buscar ciudad")
        print(findCity())
    elif decision == 4:
        print("Cantidad de pasajeros ciudad")
        print(cantCity())
    elif decision == 5:
        print("Buscar país")
        print(findDepart())
    elif decision == 6:
        print("Cantidad de pasajeros país")
        print(cantDepart())
    elif decision == 7:
        print("Salir")
        op = "no"
    else:
        print("Opción inválida")"""
        
        
#Ejercicio 2 Piedra, Papel o Tijera
"""import random

def machine():
    alea=random.randrange(3)
    opciones=["piedra", "papel", "tijera"]
    if alea==0:
        return opciones[0]
    elif alea==1:
        return opciones[1]
    elif alea==2:
        return opciones[2]
    
def play():
    alea=machine()
    desicion=input("Elige: piedra, papel o tijera?: ")
    if desicion==alea:
        result=f"Empate, sacaste {desicion} y la maquina lo mismo"
    elif desicion.lower()=="piedra" and alea=="tijera":
        result=f"Ganaste, tú sacaste {desicion} y la maquina {alea}"
    elif desicion.lower()=="piedra" and alea=="papel":
        result=f"Perdiste, tú sacaste {desicion} y la maquina {alea}"
    elif desicion.lower()=="papel" and alea=="piedra":
        result=f"Ganaste, tú sacaste {desicion} y la maquina {alea}"
    elif desicion.lower()=="papel" and alea=="tijera":
        result=f"Perdiste, tú sacaste {desicion} y la maquina {alea}"
    elif desicion.lower()=="tijera" and alea=="papel":
        result=f"Ganaste, tú sacaste {desicion} y la maquina {alea}"
    elif desicion.lower()=="tijera" and alea=="piedra":
        result=f"Perdiste, tú sacaste {desicion} y la maquina {alea}"
    else:
        result="No se entendio tu respuesta"
    return result
op="si"
while op=="si":
    print(play())
    op=input("Quieres seguir jugando?: ")"""

    
#Ejercicio 3 diccionario de notas
"""def conv_notas(dicc_notas):
    new_diccionario = {}
    for materia, nota in dicc_notas.items():
        new_diccionario[materia.upper()] = calificacion(nota)
    return new_diccionario

def calificacion(nota):
    if nota <5:
        return "Mal"
    elif nota <7:
        return "Regular"
    elif nota < 9:
        return "Bueno"
    elif nota < 10 :
        return "Muy bien"
    else:
        return "Excelente"
not_alumno = {"Matematicas": 10, "Lenguaje": 5, "Sociales": 7}
new_diccionario = conv_notas(not_alumno)
print(new_diccionario)"""