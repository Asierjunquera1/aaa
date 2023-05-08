def lista_diccionarios():
    lista=[]
    with open("madrid-airbnb-listings-small (1).csv", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            linea=linea.rstrip()
            lista1=linea.split("	")
            lista.append(lista1)
          
        lista_diccionarios=[]
        for i in range(1, len(lista)):
            diccionario={}
            for j in range(len(lista[i])):
                diccionario[lista[0][j]]=lista[i][j]
            lista_diccionarios.append(diccionario)
    return lista_diccionarios

print(lista_diccionarios())
