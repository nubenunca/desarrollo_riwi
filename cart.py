usuario={
    "name": input("escribe tu nombre"),
    "document":input("escribe tu documento")
}

# reasignar nombre 
usuario["name"]=input("ingresa nuevamente tu nombre")
# nuevo documento
usuario["document"]=input("ingresa nuevamente tu número de documento")
print(usuario)
carrito=[]
productos=[
    {
        "name":"banano",
        "price":500,
    },
    {
        "name":"manzana",
        "price":500,
    },
    {
        "name":"pera",
        "price":300,
    },
]
print(f'''Menú de acciones''')
contador = 0
for producto in productos:
    print(f"{contador} - {producto["name"]}")
    contador = contador +1

indice_seleccionado=int(input("selecciona un producto"))
cantidad= int(input("cuál es la cantidad que desea agregar"))
producto_seleccionado = productos[indice_seleccionado]
producto_seleccionado["cantidad"]=cantidad 

#agregar al carrito

carrito.append(
    producto_seleccionado
)

print(carrito)


for i in range(100):
    continuar=input("¿deseas agregar más productos al carrito")
    if continuar == "si":   
        indice_seleccionado=int(input("selecciona otro producto"))
        cantidad= int(input("cuál es la cantidad que desea agregar"))
        producto_seleccionado = productos[indice_seleccionado]
        producto_seleccionado["cantidad"]=cantidad 
        carrito.append(
            producto_seleccionado
        )
        print(carrito)
    else:
        break

print(carrito)

precio_neto=0
precio_total=0
for item in carrito:
    precio_neto=item["cantidad"]*item["price"]+precio_neto
    precio_total=item["cantidad"]*item["price"]*1.19 + precio_total
   
print("total precio neto es", precio_neto)
print("total precio neto es", precio_total)

    