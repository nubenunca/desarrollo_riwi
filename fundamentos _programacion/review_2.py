#     1. Escribir un programa que pida al usuario dos números y determine si ambos son pares.
numero1=int(input("escribe un numero"))
numero2=int(input("escribe otro numero"))
if (numero1 % 2==0) and (numero2 % 2==0):
    print(f"{numero1} y {numero2}es par")
   
# elif (numero1 % 2==0)or(numero2 % 2==0):
#     print("ambos numeros no son pares")
# else:
#     print("el numero  es impar")

#2. Crear un programa que solicite al usuario su edad y su género ('M' para masculino y 'F' para femenino) 
#y determine si la persona es elegible para jubilarse, considerando que debe tener al menos 60 años si es hombre 
#o 55 años si es mujer.

# edad=int(input("¿cual es tu edad? "))
# genero= input("seleciona el género " 
# f'''
#       [F] femenino
#       [M] masculino
#       ''' ).lower()
# f=("f")
# M=("m")


# if(edad<=60 and genero=="m") or (edad<=55 and genero=="f"):
#     print("no puedes jubiarte")
# elif (edad>=60 and genero=="m") or (edad>=55 and genero=="f"):
#     print("si puedes jubilarte")

#     3. Escribir un programa que determine si un año es bisiesto. Un año es bisiesto si es divisible por 4 pero no por 100, excepto si también es divisible por 400.

año=2000


if((año %4==0 and año %100 !=0)or año %400==0 ):
    print("es biciesto)")
else:
    print("no es año biciesto")


#     4. Crear un programa que solicite al usuario su nombre y su edad, y determine si puede obtener un descuento en el cine. Para obtener el descuento, la persona debe tener menos de 18 años o más de 60 años.
#     5. Escribir un programa que simule un sistema de autenticación simple. El programa debe solicitar al usuario un nombre de usuario y una contraseña. Si el nombre de usuario es 'admin' y la contraseña es '1234', el programa debe imprimir "Acceso concedido"; de lo contrario, debe imprimir "Acceso denegado".
#     6. Crear un programa que pida al usuario tres números y determine si al menos uno de ellos es negativo.
#     7. Solicita al usuario ingresar una temperatura en grados Celsius y conviértela a grados Fahrenheit utilizando la fórmula de conversión adecuada.
#     8. Realizar un programa que pida cargar un mes, luego verificar si dicho mes corresponde a Halloween o Navidad, validar que se pueda ingresar un mes correcto
#     9. Solicita al usuario ingresar las longitudes de los lados de un triángulo y determina si es equilátero, isósceles o escaleno.
#     10. Se ingresan por teclado tres números, si todos los valores ingresados son menores a 10, imprimir en consola "Todos los números son menores a diez"
#     11. Crea un programa que solicite al usuario el monto total de la factura y el porcentaje de propina que desea dejar. Luego, calcula el monto de la propina y muestra el total a pagar.
#     12. Pide al usuario ingresar el precio de un producto y el porcentaje de descuento aplicable. Luego, calcula el precio final después del descuento.
#     13. Se ingresan tres valores por teclado, si todos son iguales se imprime la suma del primero con el segundo y a este resultado se lo multiplica por el tercero
#     14. De un operario se conoce su sueldo y los años de antigüedad. Se pide confeccionar un programa que lea los datos de entrada e informe:
# a) Si el sueldo es inferior a 500 y su antigüedad es igual o superior a 10 años, otorgarle un aumento del 20 %, mostrar el sueldo a pagar.
# b) Si el sueldo es inferior a 500 pero su antigüedad es menor a 10 años, otorgarle un aumento de 5 %. mostrar el sueldo a pagar.
# c) Si el sueldo es mayor o igual a 500 mostrar el sueldo en pantalla sin cambios. mostrar el sueldo a pagar.

