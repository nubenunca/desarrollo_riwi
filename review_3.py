1# escribir un programa que declare una lista de números enteros y luego imprima todos los elementos de la lista.
intNumbers=[3,6,4,8,9,7]
print(intNumbers)

2#
list_names=["ana","camila","daniela"]
print(len(list_names))

3#
list_colors=["yelllow","pink","purple","blue"]
first_color=[0]
second_color=[1]
print(f'''
    {second_color}
    {first_color}
    ''', end="")
# 4#
first_number=int(input("escribe un numero"))
second_number=int(input("escribe otro numero"))
if (first_number>second_number):
    print("El primer número es mayor.")
elif (second_number>first_number):
    print("El segundo número es mayor.")
else:
    print("Los números son iguales.")

5# 5.	Escribe un programa que tome un número ingresado por el usuario e imprima "Número positivo" 
#si es mayor que cero, "Número negativo" si es menor que cero, o "El número es cero" si es igual a cero.

number_favorite=int(input("escribe tu numero favorito"))
if(number_favorite>0):
    print("número positivo")
elif(number_favorite<0):
    print("número negativo")

#6	Escribe un programa que tome dos números ingresados por el usuario y una operación (suma, resta, multiplicación o división)
# e imprima el resultado de la operación.
    
number1=int(input("escribe un numero"))
number2=int(input("escribe otro numero"))
respuesta=input("desea sumar los números")
if respuesta== "si":
    print(number1+number2)

#7Escribe un programa que busque un elemento ingresado por el usuario en una lista predefinida e imprima si el elemento está
# presente o no, para hacerlo utiliza un condicional

list_animals=["perro"
              ,"gato",
              "tiburon","estrella de mar"]
print(list_animals)
add_animal=input("quieres agregar otro animal a la lista?"  )
if add_animal.lower() == "si":
    favorite_animal=input("escribe el nombre del animal"  )
    list_animals.append(favorite_animal)
    print("animal agregado correctamente")
    print(list_animals)

#8.	Escribe un programa que sume todos los elementos de una lista de números sin usar ciclos.
list_number=[6,8,0,10,34]
total_sum= sum(list_number)
print("el total de la suma:", total_sum)

#9.	Escribe un programa que cuente el número de veces que un elemento específico aparece en una lista sin utilizar ciclos.

list_elements=["la peste","la niebla", "la caida","cumbres borrascosas","memorias del subsuelo","la caida"]
print(list_elements.count("la caida"))

#10 Escribe un programa que combine dos listas dadas y elimine los elementos duplicados sin utilizar ciclos.

list_tecnology=["aduífonos","cargador","teclado","memoria 1tb"]
list_food=["arroz","carne","papa","cargador"]
list_food.extend(list_tecnology)
print(list_food)
list_food.remove("cargador")
print(list_food)

#11	Escribe un programa que ordene una lista de números en orden ascendente sin utilizar ciclos.

list_number=[6,8,0,10,34]
list_number.sort()
print(list_number)

#12.	Escribe un programa que invierta el orden
# de los elementos en una lista sin utilizar ciclos. (usamos .reverse en lugar de .sort)


list_number=[6,8,0,10,34]
list_number.reverse()
print(list_number)

#13.	Escribe un programa que tome dos listas del mismo tamaño y las combine en una lista de tuplas
list_music=["rock","metal"]
list_favorite_music=["rock","metal"]
tupla=tuple(list_music+list_favorite_music)
print(tupla)
print(type(tupla))