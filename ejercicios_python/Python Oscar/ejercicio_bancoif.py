cap_inv=int(input("Ingrese el valor que invertirá "))
porcentaje_ganancia=int(input("Ingrese el porcentaje de ganancia que quiere "))
gan=int(cap_inv*porcentaje_ganancia)/100
nuevo_cap_inv=int(cap_inv+gan)
if gan>7000:
    print(f"Usted invirtió {cap_inv}, gano {gan} y en total quedo {nuevo_cap_inv}, le esta yendo bien, siga invirtiendo")
else:
    print(f"Usted invirtió {cap_inv}, gano {gan} y en total quedo {nuevo_cap_inv}, le esta yendo mal, debería dejar de invertir")
