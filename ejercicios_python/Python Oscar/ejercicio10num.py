"""op=0
while op<10:
    num=int(input("Ingresa el numero: "))
    if num>0:
        print(f"Tu numero es positivo, es: {num}")
    else:
        print(f"Tu numero es negativo")
    op+=1"""
numNeutro=0
numPosi=0
numNega=0
op=0
while op<5:
    numI=int(input("Ingresa el número: "))
    op+=1
    if numI==0:
        numNeutro+=1
    elif numI<0:
        numNega+=1
    else:
        numPosi+=1        
print(f"En total fueron {numNeutro} neutros, {numNega} negativos y {numPosi} positivos")