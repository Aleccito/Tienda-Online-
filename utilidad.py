from generador import *
from ordenamientos import busqueda_binaria
from timeit import default_timer as timer


def generar_lista_productos(n=50):
    return [generar_producto() for x in range(n)]

def imprimir_productos(productos):
    for p in productos:
        print(p)    

def medir_tiempo(algoritmo, lista_de_productos, key):
    inicio = timer()
    algoritmo(lista_de_productos.copy(), key=key)
    fin = timer()
    return fin - inicio

def prueba_busquedas(ids, productos):
    inicio = timer()
    for id_ in ids:
        x = busqueda_binaria(productos, id_)
    fin = timer()
    return fin - inicio
