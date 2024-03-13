# #1.Crea un diccionario llamado persona con propiedades como nombre, edad y ciudad.

# persona= {
#     "nombre":"marylin",
#     "edad":26,
#     "ciudad":"Yarumal",
#     }


# #2
# persona["ocupacion"]="investigadora"

# #3 Accede a una propiedad del diccionario persona y muestra su valor en la consola.

# print(persona["nombre"])

# #4

# libro={
#     "titulo": "La caida",
#     "autor": "Albert Camus",
#     "año de publicacion" :123,
#     }
# #print(libro)

# #5 Combina las propiedades de los diccionarios persona y libro en un nuevo diccionario llamado informacion.
# anidado=[persona|libro]
# print(anidado)

# #6 Cambia el valor de una propiedad en el diccionario persona

# libro['titulo']="la niebla"
# print(libro)

# #7Elimina una propiedad del diccionario libro.

# del libro["autor"]
# print(libro)

# #8 Crea un diccionario llamado coche con propiedades como modelo, marca y año.

# coche={
#     "modelo":2023,
#     "marca":"toyota",
#     "año":2024
# }

# #9 Muestra todas las propiedades del diccionario coche en la consola.
# print(coche)

# #10 Crea un diccionario llamado circulo con propiedades como radio y color.
# radio=30
# color="rojo"
# circulo={
#  "radio":radio,
#  "color":color,
# }

# #11 Calcula el área del círculo utilizando la fórmula A = PI* R² y muestra el resultado.
# area_circulo= (3.1416*(radio**2))
# print(area_circulo)

# #12 Crea un diccionario llamado rectángulo con propiedades como ancho y alto. 
# ancho= 40
# alto=50
# rectangulo={
#     ancho:40,
#     alto:50,
# }

# 13# Calcula el perímetro del rectángulo utilizando 
# #la fórmula P = 2 * (ancho + alto) y muestra el resultado. 

# perimetro=2*(ancho+alto)
# print(perimetro)

# 14#

# formas=[circulo|rectangulo]
# print(formas)

# #15 Crea un diccionario llamado computadora con propiedades como marca, modelo y precio. 
# precio=2000
# computadora={
#         "marca":"lenovo",
#         "modelo":"2018",
#         "precio": 2000,
# }

# #16 Muestra el precio de la computadora en la consola. 
# print(computadora["precio"])

# #17 Agrega una propiedad al diccionario computadora que indique si tiene o no una tarjeta gráfica. 

# computadora["disco_duro"]='tiene un disco duro'
# print(computadora)

# #18 Crea un diccionario llamado mascota con propiedades como nombre, especie y edad. 

# mascota={
#     "nombre":"anubis",
#     "especie":"felino",
#     "edad":7,
# }
# # 19 Muestra en la consola la especie de la mascota en mayúsculas. 

# print(mascota["especie"])

# #20 Crea un diccionario llamado fruta con propiedades como nombre y color. 

# futas={
#     "nombre":"fresa",
#     "color":"verde",
# }

# #21 Crea un diccionario llamado estudiante con propiedades como nombre, edad y calificaciones. 

estudiante={
"nombre":"camila",
 "edad":30,
 "calificaciones":{
  "ingles":5.0,
  "español":4.0
     }
 }

# #22 Muestra en la consola el promedio de las calificaciones del estudiante. 

ingles=estudiante["calificaciones"]["ingles"]
español=estudiante["calificaciones"]["español"]
promedio=(ingles+español)/2
print(promedio)

 #23 Agrega una propiedad al diccionario estudiante que indique si ha aprobado o no. 
 
if promedio >= 3:
    print("aprobaste el curso", promedio)
else:
     print("reprobaste el curso")

# #24 
bolsa={
 "tamaño":"40 cm",
"color0":"azul"
}

# #25 

print("la capacidad es",bolsa["tamaño"])

#26 Crea un diccionario llamado telefono con propiedades como marca, modelo y sistema operativo. 
telefono={
    "marca":"samsung",
    "modelo":"galaxy_s9",
    "sistema_operativo":"android",
}

#27 Muestra en la consola un mensaje indicando el sistema operativo del teléfono. 

#print({telefono["sistema_operativo"]})

telefono["memoria ram"]="256"
print(telefono)

#28 
telefonos=[
    telefono,telefono
]
indice=0
for telefono in telefonos:
    #print(f'''{indice}-{telefono["modelo"]}''')
    indice=indice+1

#29	Crea un diccionario llamado animal con propiedades como tipo y sonido. 
    animal = {
        "tipo": "león",
        "sonido": "ruuuuuuuuuuuuu"
    }   
#30 Muestra en la consola un mensaje que indique el sonido del animal. 

print(animal["sonido"])

#31 Crea un diccionario llamado vuelo con propiedades como aerolínea, número de vuelo y hora de salida. 

vuelo={
    "aerolinea":"vlm",
    "numero_de_vuelo":"4567",
    "hora_salida":"10:30"   
}

#32 Muestra en la consola un mensaje que indique la aerolínea y el número de vuelo. 
print("aerolinea:",vuelo["aerolinea"],"numero de vuelo:",vuelo["numero_de_vuelo"])

#33.	Agrega una propiedad al diccionario vuelo que represente el destino del vuelo. 
vuelo["destino_de_vuelo"]="madrid"
print(vuelo)

#34 Crea un diccionario llamado jugador con propiedades como nombre, equipo y posición. 

jugador={
    "nombre":"juan",
    "equipo":"real madrid",
    "posicion":"delantero"
}
print("nombre del jugado",jugador["nombre"],"equipo del jugador",jugador["equipo"])