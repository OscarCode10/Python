sueldo_base=int(input("Digite su sueldo base: "))
venta1=int(input("Digite su venta 1: "))
venta2=int(input("Digite su venta 2: "))
venta3=int(input("Digite su venta 3: "))
total_venta=venta1+venta2+venta3
comision=int(total_venta*(10/100))
print("Su sueldo base es de ",sueldo_base,", su venta 1 fue de ", venta1,", su venta 2 fue de ", venta2, end=", ")
print("su venta 3 fue de ",venta3,", el total de la venta ",total_venta," la comisión total fue ", comision, end=" y ")
print("su sueldo final es: ", sueldo_base+comision)