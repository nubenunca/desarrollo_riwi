productos=[
    {
    "nombre producto":"cafe juan valdez",
    "valor_producto":5000
    },
    {
    "nombre producto":"mani con pasas",
    "valor_producto":2000
    },
    {
    "nombre producto":"chocolate",
    "valor_producto":3000
    }
]
carrito=[]

# for ciclo in range(100):
#         menu_acciones=int(input(f'''selecciona una de las opciones
#                         (1) Agregar al carrito
#                         (2) Salir
#                         '''))
        
#         if menu_acciones==1:
#                 print("Agregando producto al carrito")
#         elif menu_acciones==2:
#                 break

mostrar_menu = True


print(f''' Apreciado usuario 
●	Si compra entre 5 y 10 artículos (inclusive), se aplica un descuento del 5%.
●	Si compra entre 11 y 20 artículos (inclusive), se aplica un descuento del 10%.
●	Si compra más de 20 artículos, se aplica un descuento del 15%.
''')

# primero, hago el menu

while mostrar_menu:
    menu_acciones = int(input('''Selecciona una de las opciones
                        (1) Agregar al carrito
                        (2) Salir
                        '''))
    if menu_acciones == 1:
        print("Has seleccionado, Agregar al carrito")
        # 1. Muestro la lista de productos con índice 
            
        indice=0
        for producto in productos:
            print(f''' {indice},{producto}''')
            indice=indice+1


        # 2. Creo un input para que el usuario ingrese el índice del producto que va a agregar
        indice_producto_agregar=int(input("ingresa el número correspondiente al producto que desea seleccionar"))

        # 3. Acceder al producto seleccionado a través del índice
        producto_seleccionado=productos[indice_producto_agregar]
        print(producto_seleccionado)

        # 4. Muestro input para obtener cantidad que el usuario desea comprar del producto seleccionado
        cantidad_producto_seleccionado=int(input("¿Cuantas unidades quieres? "))
        
        # 5. agregar propiedad de cantidad al producto
        producto_seleccionado["cantidad"]=cantidad_producto_seleccionado
        
        # 6. agrego el producto al carrito
        carrito.append(producto_seleccionado)
        print(carrito)
    else:
        mostrar_menu = False

# calcular descuento de acuerdo a la cantidad de productos 
# inicializamos en 0 el acumulador
# se itera sobre los elementos del carrito, accediendo a la cantidad y agregandola al acumulador
#calcular el porcentaje de descuento segun el acumulador y las condiciones. 
cantidad_total=0
for producto in carrito:
    cantidad_total=cantidad_total + producto["cantidad"]
      

descuento=0
if cantidad_total>=5 and cantidad_total<=10:
    descuento=5
elif cantidad_total>=11  and cantidad_total<=20:
    descuento=10
elif cantidad_total>=20:
    descuento=15
else:
    descuento=0
print(f'''como compraste {cantidad_total} numero de productos, tienes un porcentaje de descuento del {descuento}%''')
#DESCUENTO:
#crear variable descuentos.
#acumulador inicializa en 0, iteramos sobre los elementos del carrito, obteniendo las propiedades
#valor y cantidad se multiplican para obtener el valor total parcial, se reasigna el valor al acumulador.
#finalmente se saca el descuento. 
    
total=0
for producto in carrito:
    total=total+producto["valor_producto"]*producto["cantidad"]

total=total-total*descuento/100
print(f''' el valor total es {total}''')
