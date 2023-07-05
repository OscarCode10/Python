#Primer ejercicio
"""num1=int(input("Ingrese el numero 1 "))
num2=int(input("Ingrese el numero 2 "))

if num1==num2:
    multi=num1*num2
    print(f"Los numero son iguales, entonces se multiplican, resultado: {multi}")
elif num1>num2:
    restar=num1-num2
    print(f"El primer numero es mayor que el segundo, entonces se restan, el resultado es: {restar}")
else:
    suma=num1+num2
    print(f"El primer numero es menor que el segundo, entonces se suman, el resultado es: {suma}")"""

#Segundo ejercicio
"""num_compu=int(input("Ingresa el numero de computadoras que comprarás para poder calcular tu descuento. si son menos de 5 el descuento 10%, si son entre 5 contandolo y menos de 10 descuento sera de 20%, y si son más de 10 contandolo el decuento sera del 40% "))
total=int(num_compu*15000)
if num_compu<5:
    print(f"El total de pagar es {total}, pero con 10% de descuento son {int(total*0.9)} a pagar")
elif num_compu>=5 and num_compu<10:
    print(f"El total de pagar es {total}, pero con 20% de descuento son {int(total*0.8)} a pagar")
else:
    print(f"El total de pagar es {total}, pero con 40% de descuento son {int(total*0.6)} a pagar")"""
    
#Tercer ejercicio
"""numLlantas=int(input("Ingrese el numero de llantas que comprará, si compra menos de 5 cada una valdrá 300mil, si compra entre 5 contandolo y 10 cada una valdrá 250mil y si compra más de 10 contandolo cada una valdrá 200mil "))
if numLlantas<5:
    print(f"Usted compro {numLlantas}, por lo tanto le valdrá cada una 300, en total pagará {numLlantas*300}mil")
elif numLlantas>=5 and numLlantas<10:
    print(f"Usted compro {numLlantas}, por lo tanto le valdrá cada una 250, en total pagará {numLlantas*250}mil")
else:
    print(f"Usted compro {numLlantas}, por lo tanto le valdrá cada una 200, en total pagará {numLlantas*200}mil")"""
    
#Cuarto ejercicio
"""pregunta1=input("¿Colón decubrió América? ")
if pregunta1=="si":
    pregunta2=input("¿La independencia de México fue en el año 1810? ")
    if pregunta2=="si":
        pregunta3=input("¿The Doors fue un grupo de rock americano? ")
        if pregunta3=="si":
            print("¡GANASTEEEE!")
        else:
            print("Lo siento, casi ganas")
    else:
        print("Lo siento, no era la respuesta, pero hiciste una bien")
else:
    print("Lo siento, la respuesta no fue correcta")"""
    
#Quinto ejercicio
num1=int(input("Ingrese el primer número "))
num2=int(input("Ingrese el segundo número "))
num3=int(input("Ingrese el tercer número "))
if num1>num3 and num1>num2:
    print(f"El numero 1 es el mayor, el numero es: {num1}")
elif num2>num1 and num2>num3:
    print(f"El numero 2 es el mayor, el numero es: {num2}")
elif num3>num1 and num3>num2:
    print(f"El numero 3 es el mayor, el numero es: {num3}")
elif num1==num2 and num2==num3:
    print(f"Los tres numero son iguales: {num1}")
