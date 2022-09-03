centinela=100
i=None
print("**MENU EMPA EMPA EMPANADAS**")
print("1.Crear una empanada")
print("2.Mostrar empanadas")
print("0.salir")
diccionarios={
    'nombre':"",
    'ingrediente1':"",
    'ingrediente2':"",
    'ingrediente3':"",
    'preciofab':"",
    'preciovent':""
}
while(centinela!=0):
    centinela=int(input("Digita una opcion: "))
    if(centinela==1):
      i=input("Digite el nombre de la empanada: ")
      diccionarios['nombre']=i
      i=input("Digite el ingrediente 1: ")
      diccionarios['ingrediente1']=i
      i=input("Digite el ingrediente 2: ")
      diccionarios['ingrediente2']=i
      i=input("Digite el ingrediente 3: ")
      diccionarios['ingrediente3']=i
      i=input("Digite el precio de fabricacion: ")
      diccionarios['preciofab']=i
      i=input("Digite el precio de venta: ")
      diccionarios['preciovent']=i
    elif(centinela==2):
        for clave,valor in diccionarios.items():
         print(f"{clave} = {valor}")
    elif(centinela==0): break #Break sirve para parar el programa ignorando el resto del codigo, como un freno de mano
    else: print ("Digite una opcion valida")
else:
    print("termine")