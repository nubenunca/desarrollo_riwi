# Requerimientos: 
# 1.  El programa debe permitir a veterinaria Dalí gestionar sus pacientes. 
# 2.  Debe utilizar una lista para mantener guardados los pacientes, donde cada mascota se representa como una lista o diccionario con su 
#nombre, identificación dueño, raza, edad (en años) , estado (si está aún en la veterinaria o no ) y diagnóstico. 

pacientes=[
   { "nombre_mascota":"Luna",
    "edad":"3años",
    "identificacion_propietario":"1029209292",
    "estado":"activo",
    "diagnostico":"fractura"
   },
   {
    "nombre_mascota":"Luna",
    "edad":"3años",
    "identificacion_propietario":"1029209292",
    "estado":"inactivo",
    "diagnostico":"fractura"
   }
]
for _ in range(100):
    desplegar_menu = input(f"""Desplegar Menu: si/no """)
    if desplegar_menu == "si": 
        print(f"""MENU DE ACCIONES
            (1) registrar paciente
            (2) actualizar información de un paciente
            (3) ver paciente activos
            (4) ver pacientes inactivos
            (5) salir del programa
            """)

        seleccion_menu=int(input("Seleccione una opición: "))
        if seleccion_menu==1:
            print("registrar un paciente")
            nombre_nuevo_paciente=input("ingresa el nombre de tu macota: ")
            edad_nuevo_paciente=input("ingresala edad de tu mascota: ")
            Indentificacion_nuevo_paciente=input("Ingresa la identificación del propietario: ")
            estado_nuevo_paciente=(input(f'''' ¿la mascota está en la clínica? activo, inactivo: '''))
            diagnostico_nuevo_paciente=input("Ingresa el diagnostico de la mascota: ")
            nuevo_paciente={
                'nombre_mascota':nombre_nuevo_paciente,
                'edad':edad_nuevo_paciente,
                "identificacion_propietario":Indentificacion_nuevo_paciente,
                "estado":estado_nuevo_paciente,
                "diagnostico":diagnostico_nuevo_paciente
                }
            pacientes.append(nuevo_paciente)
            print(pacientes)

        elif seleccion_menu == 2:
            print("actualizar la información de un paciente")
            contador=0
            for paciente in pacientes:
                print(f'''({contador}) {paciente["nombre_mascota"]}, {paciente["identificacion_propietario"]}''')
                contador+=1

            id_del_paciente= int(input('ingresa el número correspondiente a la mascota que quieres actualizar: '))
            paciente_a_modificar=pacientes[id_del_paciente]
            nombre=input("ingresa el nuevo nombre")
            paciente_a_modificar["nombre_mascota"]=nombre
            edad_actual=input("ingresa edad actual")
            paciente_a_modificar["edad"]=edad_actual
            print(pacientes)

        elif seleccion_menu == 3:
            print("estos son los pacientes activos")
            contador=0
            for paciente in pacientes:
                    if paciente["estado"]== "activo":
                         print(paciente)
                    contador=+1

        elif seleccion_menu == 4:
            print("estos son los pacientes activos")
            contador=0
            for paciente in pacientes:
                    if paciente["estado"]== "inactivo":
                         print(paciente)
                    contador=+1
        elif seleccion_menu== 5:
             print("el software se ha cerrado corrrectamente")

    else:
        break
