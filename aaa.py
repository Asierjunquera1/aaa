def lista_alojamientos():
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


def contar_alojamientos_por_distrito(alojamientos):
    alojamientos_por_distrito = {}

    for alojamiento in alojamientos:
        distrito = alojamiento["host_neighbourhood"]
        if distrito in alojamientos_por_distrito:
            alojamientos_por_distrito[distrito] += 1
        else:
            alojamientos_por_distrito[distrito] = 1

    return alojamientos_por_distrito

def alojamientos_con_mas_plazas(alojamientos, numero_ocupantes):
    lista_alojamientos=[]
    for i in range(len(alojamientos)):
        if int(alojamientos[i]["bedrooms"])>=numero_ocupantes:
            lista_alojamientos.append(alojamientos[i])


