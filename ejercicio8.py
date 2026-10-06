nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
nota1 = float(input("Ingrese nota 1: "))
nota2 = float(input("Ingrese nota 2: "))
nota3 = float(input("Ingrese nota 3: "))
promedio = (nota1+nota2+nota3)/3
print("El promedio total es:", promedio)
if promedio >= 71:
    print("Aprobado")
else :
    print("No aprobado")

