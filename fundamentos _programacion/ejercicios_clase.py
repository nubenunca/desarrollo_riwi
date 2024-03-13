#1
list=[9,6,2,1,9,5]
CantidadDeApariciones=list.count(5)
if CantidadDeApariciones >=1:
    print("el numero 5 esta en la lista")

#2

lenguajesDProgramacion=["Java"
    ,"Python",
            "PHP",
            "SQL",
            "Ruby",]
CantidadDeApariciones=lenguajesDProgramacion.count("Python")

if CantidadDeApariciones>=1:
    print("Python esta en la lista")

#4
nombres=["ana","maria","camila","marcela","camila","luisa"]
LongitudDeLaLista=len(nombres)
if LongitudDeLaLista>5:
    print("la lista es larga")
else:
    print("la lista es corta")

#5 
list_of_numbers=[3,5,0,9,10,4,3]
first_number= list_of_numbers[0]
last_number= list_of_numbers[-1]

if (first_number == last_number):
    print("el primer y el ultimo numero son iguales")

#6
list_of_ages=[31,50,60,9,10,24,30]

for age in list_of_ages:
    if (age<18):
        print("hay personas menores de edad en la lista")
        break

list_of_ages.sort()
if (list_of_ages[0]<18):
    print("hay personas menores de edad en la lista")

fruits=["pera","manzana","banano","durazno"]
for fruit in fruits:
    if(fruit=="manzana"):
        print("hay manzanas en la lista")
        break

#7
if("manzana" in fruits):
    print("si hay manzanas en la lista")

if(fruits.count("manzana")>=2):
    print("si hay manzanas")

#8
    
list_of_numbers=[3,5,0,9,10,4,3]

total=0
for number in list_of_numbers:
    total=number+total
print(total)

#9
list_names=["angela",
            "camila",
            "daniela"
            ,"alejandra"]

list_names.sort()
print(list_names)

for letra_a in list_names:
        print(list_names[0:2])
        break

#10
list_ratings=[1.0,2.0,5.0,6.0]
list_ratings.sort()
if (list_ratings[0]<=1.0):
    print("hay calificaciones bajas en la lista")

frutas=["banana","manzana","durazno"]
for fruta in frutas:
    print(fruta)

   

#ejercicio clase
        
# Numbers=[]
# Number1=int(input("ingrese el numero 1"))
# Number2=int(input("ingrese el numero 1"))
# Number3=int(input("ingrese el numero 1"))
# Number4=int(input("ingrese el numero 1"))
# Number5=int(input("ingrese el numero 1"))

# Numbers.Append(Number1)
# Numbers.Append(Number2)
# Numbers.Append(Number3)
# Numbers.Append(Number4)
# Numbers.Append(Number5)
#ciclo for    
# for numero_vueltas in range(5):
#    number=int(input("ingrese un numero"))
   
# Numbers.append(number)

#ciclo while
# Numbers=[]
# Numbers=0
# while Numbers!=5:
#     number=int(input("ingrese un numero"))
# Numbers.append(number)
# print(Numbers)

#Ejercicio con el cliclo for para cambiar elementos a traves de los metodos
lista_estudiantes=[]   

ingresar_otro_estudiante="si"
while ingresar_otro_estudiante =="si":

    name=input("escribe tu nombre: ")
    apellido=input("escribe tu apellido: ")
    email= input("escribe tu correo: ")#variable
    edad= int(input("escribe tu edad: "))
    direccion=input("escribe la direccion de tu casa: ")

#ejemplo diccionarios

    estudiantes={
        "name":name,
        "apellido":apellido,
        "email":email,
        "edad":edad,
        "direccion":direccion,
    }

    lista_estudiantes.append(estudiantes)
    respuesta= input("¿vas a agregar otro estudiante? =>")
    if respuesta!="si":
        ingresar_otro_estudiante=False
print(lista_estudiantes)



for i in lista_estudiantes: #ciclo for
    print(f'''{i["name"].upper()},
        {i["apellido"].capitalize()},
        {i["email"].lower()},
        {i["edad"]},
        {i["direccion"].title()}''') 


#impresion el numero de veces #los metodos siempre finalizan en parentesis
#title() sirve para poner cada letra en mayuscula
#capitalize() sirve para poner la letra inicial en mayuscula


