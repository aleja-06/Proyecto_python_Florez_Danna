

def AñadirUsuarios():
    import json 
     


    with open ('usuarios.json', "r" ) as file:
        mijson = json.load(file)

def mainusuario():
     
    estado = "usuario"
    nuevo_id = max([usuario["id"] for usuario in mijson['datos']['usuarios']], default=0) + 1

    nuevo_usuario = {}
    nuevo_usuario['id'] = nuevo_id
    nuevo_usuario['Identificacion'] = int(input("Escriba el número de identificación: "))
    nuevo_usuario['Nombre'] = input("Escriba el nombre: ")
    nuevo_usuario['Apellido1'] = input("Escriba el apellido 1: ")
    nuevo_usuario['Direccion'] = input("Escriba la dirección: ")
    nuevo_usuario['Contacto'] = int(input("Escriba el número de celular: "))
     
      
    mijson['datos']['usuarios'].append(nuevo_usuario)

    with open('usuarios.json', 'w') as file:
           json.dump( nuevo_usuario , file, indent=4)



        