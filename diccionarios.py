diccionarios={
    'nombre':"Juan", #Clave:Value=Item
    'edad':33,
    'estudiante':True,
    'tieneVoz':False,
    'nacimiento':"2022-05-12"
}

print(diccionarios)

#Recorriendo un DICCIONARIO

for clave,valor in diccionarios.items():
    print(clave)
    print(valor)