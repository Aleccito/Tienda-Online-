from utilidad import *
from ordenamientos import insertion_sort, bubble_sort, merge_sort
from generador import generar_ids

def main():
    productos = generar_lista_productos()
    print("Lista de productos generada \n")
    imprimir_productos(productos)

    print("\n Ordenamientos por precio ascendente ")
    print(f"Insertion Sort: {medir_tiempo(insertion_sort, productos, key=lambda p: p.precio):.6f} s")
    print(f"Bubble Sort:    {medir_tiempo(bubble_sort, productos, key=lambda p: p.precio):.6f} s")
    print(f"Merge Sort:     {medir_tiempo(merge_sort, productos, key=lambda p: p.precio):.6f} s")
    
    print("\n Ordenamientos por rating descendente ")
    print(f"Insertion Sort: {medir_tiempo(insertion_sort, productos, key=lambda p: -p.rate):.6f} s")
    print(f"Bubble Sort:    {medir_tiempo(bubble_sort, productos, key=lambda p: -p.rate):.6f} s")
    print(f"Merge Sort:     {medir_tiempo(merge_sort, productos, key=lambda p: -p.rate):.6f} s")
    
    print("\n BUSQUEDA BINARIA")
    productos_ordenados = merge_sort(productos.copy(), key=lambda p: p.id_product)
    
    id_existentes = []
    productos_muestra = random.sample(productos_ordenados, 10)
    for producto in productos_muestra:
        id_existentes.append(producto.id_product)

    id_inexistentes = [generar_ids() for x in range(10)]
    

    print(f"Tiempo búsqueda binaria existentes:   {prueba_busquedas(id_existentes,productos_ordenados):.6f} s")
    print(f"Tiempo búsqueda binaria inexistentes:   {prueba_busquedas(id_inexistentes,productos_ordenados):.6f} s")

    
if __name__ == "__main__":
    main()


    