def insertion_sort(productos, key=lambda x: x):
    n = len(productos)
    for i in range(1, n):
        current = productos[i]
        j = i - 1
        while j >= 0 and key(productos[j]) > key(current):
            productos[j + 1] = productos[j]
            j -= 1
        productos[j + 1] = current
    return productos

def bubble_sort(productos, key=lambda x: x):
    permutation = True
    iteracion = 0
    while permutation:
        permutation = False
        iteracion += 1
        for i in range(0, len(productos) - iteracion):
            if key(productos[i]) > key(productos[i + 1]):
                productos[i], productos[i + 1] = productos[i + 1], productos[i]
                permutation = True
    return productos


def merge_sort(productos, key=lambda x: x):
    if len(productos) <= 1:
        return productos

    mid = len(productos) // 2
    left = merge_sort(productos[:mid], key)
    right = merge_sort(productos[mid:], key)

    return merge(left, right, key)

def merge(left, right, key):
    resultado = []
    i = j = 0

    while i < len(left) and j < len(right):
        if key(left[i]) <= key(right[j]):
            resultado.append(left[i])
            i += 1
        else:
            resultado.append(right[j])
            j += 1

    resultado.extend(left[i:])
    resultado.extend(right[j:])
    return resultado

def busqueda_binaria(productos, objetivo_id):
    izquierda = 0
    derecha = len(productos) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        actual_id = productos[medio].id_product

        if actual_id == objetivo_id:
            return productos[medio]
        elif actual_id < objetivo_id:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return None


