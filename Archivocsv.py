import random



def get_path_actual(bicicletas:str)->str:
    """Devuelve el directorio actual

    Args:
        bicicletas (str): bicicletas es el nombre del archivo

    Returns:
        str: el directorio actual
    """
    if type(bicicletas) is not str:
        raise TypeError("El nombre del archivo no es de tipo str")
    import os
    directorio_actual = os.path.dirname(__file__)
    return os.path.join("./Escritorio/bicicletas")



#1)
def cargar_un_csv(bicicletas:str)->list:
    """carga un archivo de csv

    Args:
        ruta_del_archivo (str):Es la ruta del archivo

    Returns:
        list: la lista de bicicletas
    """
    if type("./C:/Users/Admin/OneDrive/Escritorio/bicicletas.csv") != str:
            raise TypeError("La ruta no es de tipo str")
    with open(get_path_actual("C:/Users/Admin/OneDrive/Escritorio/bicicletas.csv"), "r", encoding="utf-8") as archivo_csv:
        list = []
       
        encabezado = archivo_csv.readline().strip("\n").split(",")

        for linea in archivo_csv.readlines():
            bici = {}
            linea = linea.strip(",").split(",")
            id_bike, nombre, tipo, tiempo = linea
            bici["id_bike"] = int(id_bike)
            bici["nombre"] = nombre
            bici["tipo"] = tipo
            bici["tiempo"] = int(tiempo)
            list.append(bici)
            print(list)
        return list, encabezado



#3)

def poner_tiempo(lista:list):
    """Mapea cada tipo de bici y le calculara aleatoriamente un valor de timepo(de entre 50 a 120)

    Args:
        lista (list): lista de diccionarios de bicicletas
    """
    for bici in lista:
        bici['tiempo'] = random.randint(50, 120)

for bici in list:
    print(f"Bicicleta {bici['id']} ({bici['modelo']}): {bici['tiempo']} minutos")


#4)
def informar_ganador(list):
    """Informa quien llegó primero, calculando el menor tiempo. Si hay empate, tambien lo informa 

    Args:
        lista (list): lista de diccionarios de bicicletas
    """
    bandera_primer_elemento = True
    menor_tiempo = list[0]
    for el in list:
        if bandera_primer_elemento == True or menor_tiempo['tiempo'] > el['timepo']:
            menor_tiempo = el
            bandera_primer_elemento = False
    ganadores = [bici for bici in list if bici['tiempo'] == menor_tiempo]
    if len(ganadores) == 1:
        print(f"El ganador es: {ganadores[0]['nombre']} con un tiempo record de {menor_tiempo} minutos.")
    else:
        print(f"Hubo un empate entre: {[ganador['nombre'] for ganador in ganadores]} con un tiempo record de {menor_tiempo} minutos.")

#6)
def promedio_tiempo_bicicletas(lista: list):
    """saca el promedio del tiempo, segun su tipo

    Args:
        lista (list): lista de diccionarios de bicicletas
    """

    tiempo_acumulado = 0
    for el in lista:
        tiempo_acumulado += float(el['tiempo'])
    promedio_time_bicis = tiempo_acumulado / len(lista)
    print(f"El promedio de tiempo en las bicis es: {promedio_time_bicis}")

poner_tiempo(list)