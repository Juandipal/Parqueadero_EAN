""""
Entradas:
Nombre-->str-->n
Numerocedula-->int-->cd
tipodevehiculo-->int-->tipo
Registroplaca-->str-->placa
Salida:
valorapagar-->int-->vpag
tipoparqueadero-->int-->tipo
valorapagarcondescuento-->desc
lugardeparqueo-->int-->parqueo
"""
parquedero=[[1,1,"ocupado",1],[2,1,"ocupado",1],[3,1,"ocupado",1],[4,1,"ocupado",1],[5,1,"libre",1],[6,1,"ocupado",1],[7,1,"libre",1],[8,1,"libre",1],[9,1,"ocupado",1],[10,1,"libre",1],[11,1,"libre",1],[12,1,"ocupado",1],[13,1,"libre",1],[14,1,"libre",1],[15,1,"ocupado",1],[16,1,"ocupado",1],[17,1,"libre",1],[18,1,"ocupado",1],[19,1,"libre",1],[20,1,"ocupado",1],[21,1,"ocupado",1],[22,1,"ocupado",1],[23,1,"ocupado",1],[24,1,"ocupado",1],[25,1,"ocupado",1],[26,1,"ocupado",1],[27,1,"libre",1],[28,1,"ocupado",1],[29,1,"libre",1],[30,1,"ocupado",1],[31,1,"libre",1],[32,1,"ocupado",1],[33,1,"libre",1],[34,1,"ocupado",1],[35,1,"ocupado",1],[36,1,"ocupado",1],[37,1,"ocupado",1],[38,1,"libre",1],[39,1,"ocupado",1],[40,1,"libre",1],[41,1,"libre",1],[42,1,"ocupado",1],[43,1,"libre",1],[44,1,"libre",1],[45,1,"ocupado",1],[46,1,"ocupado",1],[47,1,"ocupado",1],[48,1,"libre",1],[49,1,"ocupado",1],[50,1,"ocupado",1],[51,1,"ocupado",1],[52,1,"libre",1],[53,1,"libre",1],[54,1,"libre",1],[55,1,"ocupado",1],[56,"ocupado",1],[57,1,"ocupado",1],[58,1,"ocupado",1],[59,1,"libre",1],[60,1,"libre",1],[61,2,"ocupado",1],[62,2,"ocupado",1],[63,2,"ocupado",1],[64,2,"ocupado",1],[65,2,"ocupado",1],[66,2,"ocupado",1],[67,2,"ocupado",1],[68,2,"ocupado",1],[69,2,"ocupado",1],[70,2,"ocupado",1],[71,3,"ocupado",1],[71,3,"ocupado",1],[72,3,"ocupado",1],[73,3,"ocupado",1],[74,3,"ocupado",1],[75,3,"libre",1],[76,3,"ocupado",1],[77,3,"libre",1],[78,3,"ocupado",1],[79,3,"ocupado",1],[80,3,"ocupado",1],[81,1,"ocupado",2],[82,1,"ocupado",2],[83,1,"ocupado",2],[84,1,"ocupado",2],[85,1,"libre",2],[86,1,"ocupado",2],[87,1,"libre",2],[88,1,"ocupado",2],[89,1,"ocupado",2],[90,1,"ocupado",2],[91,1,"ocupado",2],[92,1,"ocupado",2],[93,1,"ocupado",2],[94,1,"libre",2],[95,1,"ocupado",2],[96,1,"libre",2],[97,1,"libre",2],[98,1,"ocupado",2],[99,1,"ocupado",2],[100,1,"libre",2],[101,1,"libre",2],[102,1,"ocupado",2],[103,1,"ocupado",2],[104,1,"ocupado",2],[105,1,"ocupado",2],[106,1,"ocupado",2],[107,1,"ocupado",2],[108,1,"libre",2],[109,1,"ocupado",2],[110,1,"ocupado",2],[111,1,"ocupado",2],[112,1,"ocupado",2],[113,1,"ocupado",2],[114,1,"ocupado",2],[115,1,"ocupado",2],[116,1,"ocupado",2],[117,1,"ocupado",2],[118,1,"ocupado",2],[119,1,"ocupado",2],[120,1,"ocupado",2],[121,1,"ocupado",2],[122,1,"ocupado",2],[123,1,"ocupado",2],[124,1,"ocupado",2],[125,1,"ocupado",2],[126,1,"ocupado",2],[127,1,"ocupado",2],[128,1,"ocupado",2],[129,1,"ocupado",2],[130,1,"ocupado",2],[131,1,"libre",2],[132,1,"libre",2],[133,1,"libre",2],[134,1,"libre",2],[135,1,"libre",2],[136,1,"libre",2],[137,1,"libre",2],[138,1,"libre",2],[139,1,"libre",2],[140,1,"ocupado",2],[141,2,"ocupado",2],[142,2,"ocupado",2],[143,2,"ocupado",2],[144,2,"ocupado",2],[145,2,"ocupado",2],[146,2,"ocupado",2],[147,2,"ocupado",2],[148,2,"ocupado",2],[149,2,"ocupado",2],[150,2,"ocupado",2],[151,3,"ocupado",2],[152,3,"ocupado",2],[153,3,"ocupado",2],[154,3,"ocupado",2],[155,3,"ocupado",2],[156,3,"ocupado",2],[157,3,"ocupado",2],[158,3,"ocupado",2],[159,3,"ocupado",2],[160,3,"ocupado",2],[161,1,"ocupado",3],[162,1,"ocupado",3],[163,1,"ocupado",3],[164,1,"ocupado",3],[165,1,"ocupado",3],[166,1,"ocupado",3],[167,1,"ocupado",3],[168,1,"ocupado",3],[169,1,"ocupado",3],[170,1,"ocupado",3],[171,1,"ocupado",3],[172,1,"ocupado",3],[173,1,"ocupado",3],[174,1,"ocupado",3],[175,1,"ocupado",3],[176,1,"ocupado",3],[177,1,"ocupado",3],[178,1,"ocupado",3],[179,1,"ocupado",3],[180,1,"ocupado",3],[181,1,"ocupado",3],[182,1,"ocupado",3],[183,1,"ocupado",3],[184,1,"ocupado",3],[185,1,"ocupado",3],[186,1,"ocupado",3],[187,1,"ocupado",3],[188,1,"ocupado",3],[189,1,"ocupado",3],[190,1,"ocupado",3],[191,1,"ocupado",3],[192,1,"ocupado",3],[193,1,"ocupado",3],[194,1,"ocupado",3],[195,1,"ocupado",3],[196,1,"ocupado",3],[197,1,"ocupado",3],[198,1,"ocupado",3],[199,1,"ocupado",3],[200,1,"ocupado",3],[201,1,"ocupado",3],[202,1,"ocupado",3],[203,1,"ocupado",3],[204,1,"ocupado",3],[205,1,"ocupado",3],[206,1,"ocupado",3],[207,1,"ocupado",3],[208,1,"ocupado",3],[209,1,"ocupado",3],[210,1,"ocupado",3],[211,1,"ocupado",3],[212,1,"ocupado",3],[213,1,"ocupado",3],[214,1,"ocupado",3],[215,1,"ocupado",3],[216,1,"ocupado",3],[217,1,"ocupado",3],[218,1,"ocupado",3],[219,1,"ocupado",3],[220,1,"ocupado",3],[221,2,"ocupado",3],[222,2,"ocupado",3],[223,2,"libre",3],[224,2,"libre",3],[225,2,"libre",3],[226,2,"libre",3],[227,2,"libre",3],[228,2,"ocupado",3],[229,2,"ocupado",3],[230,2,"ocupado",3],[231,3,"ocupado",3],[232,3,"ocupado",3],[233,3,"ocupado",3],[234,3,"ocupado",3],[235,3,"ocupado",3],[236,3,"ocupado",3],[237,3,"libre",3],[231,3,"ocupado",3],[239,3,"libre",3],[240,3,"libre",3]]
#tipo parquedero[fila][1]
#reserva parquedero[fila][2]
print("¡¡BIENVENIDO AL PARQUEADERO DE LA UNIVERSIDAD EAN!! 🥳 🤓")
#Fecha y hora------------------------------------
from datetime import datetime 
from pytz import timezone 

fmt = "%Y-%m-%d %H:%M:%S " 
timezonelist = ['America/Bogota'] 

for zone in timezonelist: 
    now_time = datetime.now(timezone(zone)) 
    print(now_time.strftime(fmt))
##--------------------------------------------
#tiempo entrada carro
import time
tiempo1_min=time.gmtime()
he=(tiempo1_min[3]*60)
me=tiempo1_min[4]
he_min=me+he


while True:
  tipo_ingreso=int(input("Si eres empleado del parqueadero ingresa 1 si eres usuario 0: "))
  try:
    if(tipo_ingreso>=0 and tipo_ingreso<=1):
       break
    else:
      print("La opcion seleccionada no es válida ⚠️")  
  except:
   print("Intente de nuevo! ⚠️") 
while (tipo_ingreso==1):
 empleado=(input("Digite Usuario: "))
 contraseña=((input("Digite contraseña: ")))
 lista=["erika","1234"]
 print("Bienvenido 🎉")
 break
 

while(tipo_ingreso==0):
    n=input("Ingrese su rol en la universidad: ")
    

    while True:
        cd=input("Ingrese su número de cédula: ")
        try:
         cd=int(cd)
         if(cd>0):
           break
         else:
          print("El número de cedula debe ser positivo⚠️")  
        except:
         print("Ingrese solo numero su cédula ⚠️")  
    

    while True:
      nombre_usuario=input("Ingrese su nombre: ")
      placa=input("ingrese placa: ")
      tipo_vehiculo=int(input("ingrese tipo de vehiculo: 1-->para carro 🚗, 2-->para moto 🏍️, 3-->para bicicleta🚲: "))
      ingreso=[["diana casas",1,"efr134",1,1],["brayan torres",1,"asd123",2,1]]
      for fila in range(0,240):
        if(parquedero[fila][1]==tipo_vehiculo and parquedero[fila][2]=="libre"):
         parquedero[fila][2]="ocupado"
         usuario=[nombre_usuario,tipo_vehiculo,placa,parquedero[fila][0],parquedero[fila][3]]
         ingreso.append(usuario)
      for fila in range(len(ingreso)):
        if(ingreso[fila][2]==placa):
          print("Estimad@ "+nombre_usuario+"\n"+"Su número de parqueadero es: "+str(ingreso[fila][3])+"\n"+"Su piso es el No: "+str(ingreso[fila][4]))
          print("Hora de ingreso: ",(now_time.strftime(fmt)))
          break
          
  #cuentas cedulas hayprint(listaCc.count(cc))
    while True: 
      cc=int(input("Ingrese su CC para saber si cuenta con un descuento 🤑  💲: "))
    listaCc=[1019134469,1019134469,1019134469,1019134469]
    listaCc.append(cc)
    if(listaCc.count(cc)==5):
        print("tiene descuento del 20% por su fidelidad 💲",cc)
    else:
       print("no tine descuento ♦️ : ",cc)
       print("Muchas gracias por confiar en nosotros, dirijase a su parqueadero ") 
  

#total apgar
import time
import random
n=random.randint(0,1000)
tiempo2_min=time.gmtime()
hs=(tiempo2_min[3]*60)
ms=tiempo2_min[4]
hs_min=me+he
x=hs-he
if(tipo_ingreso==0):
  if(x<0):
    if(listaCc.count(cc)==5):
      if(tipo_vehiculo==1):
        t1=he_min-1400
        T=t1+hs_min
        tp=(T+n-((T+n)*0.2))*80
        print("Total a pagar "+str(tp)+" COP")
      elif(tipo_vehiculo==2):
        t1=he_min-1400
        T=t1+hs_min
        tp=(T+n-((T+n)*0.2))*60
        print("Total a pagar "+str(tp)+" COP")
      else:
        t1=he_min-1400
        T=t1+hs_min
        tp=(T+n-((T+n)*0.2))*40
        print("Total a pagar "+str(tp)+" COP")
    else:
      if(tipo_vehiculo==1):
        t1=he_min-1400
        T=t1+hs_min
        tp=(T+n)*80
        print("Total a pagar "+str(tp)+" COP")
      elif(tipo_vehiculo==2):
        t1=he_min-1400
        T=t1+hs_min
        tp=(T+n)*60
        print("Total a pagar "+str(tp)+" COP")
      else:
        t1=he_min-1400
        T=t1+hs_min
        tp=(T+n)*40
        print("Total a pagar "+str(tp)+" COP")
  else:
    if(listaCc.count(cc)==5):
      if(tipo_vehiculo==1):
        t=hs_min-he_min
        tp=((t+n)*0.2)*80
        print("Total a pagar "+str(tp)+" COP")
      elif(tipo_vehiculo==2):
        t=hs_min-he_min
        tp=((t+n)*0.2)*60
        print("Total a pagar "+str(tp)+" COP")
      else:
        t=hs_min-he_min
        tp=((t+n)*0.2)*40
        print("Total a pagar "+str(tp)+" COP")
    else:
      if(tipo_vehiculo==1):
        t=hs_min-he_min
        tp=(t+n)*80
        print("Total a pagar "+str(tp)+" COP")
      elif(tipo_vehiculo==2):
        t=hs_min-he_min
        tp=(t+n)*60
        print("Total a pagar "+str(tp)+" COP")
      else:
        t=hs_min-he_min
        tp=(t+n)*40
        print("Total a pagar "+str(tp)+" COP")
      