import json








Usuarios= []
Usuarios= [ {

    "nombre": "",
    "direccion": "",
    "contacto": "",
    "plan que usa": "",
    "id": ""

 }]



        

with open ("usuarios.json", "w") as file:
  json.dump (Usuarios, file , indent=4)


servicios= []
servicios= [{
  
  "Internet Fibra Optica":"",
  "Plan Pospago": "",
  "Plan Prepago": "",

}]

with open ("servicios.json", "w") as file:
  json.dump (servicios, file , indent=4)
  


    
