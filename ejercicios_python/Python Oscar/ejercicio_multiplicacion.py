"""op=1
decision=int(input("Ingrese el número del que quiere ver la tabla "))
while op<=10:
    print(f"Tu número fue {decision}, {decision} x {op} = {decision*op}")
    op+=1"""

num=int(input("Ingresa el número que quieres multiplicar"))
for op in range(1,11):
    print(f"Tu número fue {num}, {num} x {op} = {num*op}")
