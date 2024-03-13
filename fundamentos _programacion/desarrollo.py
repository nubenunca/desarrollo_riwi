


# usuario=input("ingresa tu usuario")
# contraseña=int(input("ingresa tu contraseña"))

# if (usuario=="admin" and contraseña==1234):
#     print("Puedes operar en el programa")
# else:
#     print("acceso restringido")


# userlogueado=True
# if(userlogueado==True):
#     print("Bienvenido")
# else:
#     print("suerte")


# comprar=1
# devolver=2
# cerrar=3


print(''' 
      [Supermercado RIWI]''' )
print("OPCIONES=>")

print('''
[1]vas a comprar
[2]vas a devolver
[3]cerrar programa
      ''')
dinero=True
opcion=int(input("seleccione una opcion"))

if (opcion==1 or dinero==True):
    print("vas a comprar")

elif(opcion==2):
    print(" vas a devolver")

elif(opcion==3):
    print("adios")

else:
    print("ingresaste una opcion invalida")