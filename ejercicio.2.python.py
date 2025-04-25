"""Pide dos números decimales al usuario 
Realiza operaciones básicas como suma, resta, multiplicación y división.
Muestra los resultados en pantalla, con la división mostrando 
sólo dos numerales"""

numero1 = float(input("digita número"))
numero2 = float(input("digita número"))

#Realiza operaciones básicas

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

print(f"El resultado de la división es {division:.2f}")
print(f"El resultado de la multiplicacion es {multiplicacion}")
print(f"El resultado de la resta es {resta}")
print(f"El resultado de la suma es {suma}")