from producto import Productos
import random, string

PRODUCTOS_POR_CATEGORIAS = {
    "Belleza": ["Perfume", "Maquillaje", "Crema facial", "Crema corporal", "Espuma Limpiadora"],
    "Tecnologia": ["Monitor", "Laptop", "PC", "Raton", "Teclado", "Auriculares", "PS5", "Nintendo Wi-U"],
    "Calzados": ["Zapatillas", "Botas", "Sandalias", "Zapatos"],
    "Ropa": ["Camiseta", "Pantalón", "Abrigo", "Medias", "Gorra"],
    "Casa": ["Estufa", "Nevera", "Lavadora", "Mesa"]
}

PRECIO_POR_CATEGORIA = {
    "Belleza": (20.0, 200.0),
    "Tecnologia": (300.0, 1000.0),
    "Calzados": (30.0, 200.0),
    "Ropa": (15.0, 100.0),
    "Casa": ( 600.0, 1500.0)
}




def generar_ids():
    return f"ID-{''.join(random.choices(string.ascii_uppercase + string.digits, k=7))}"
    
      
def generar_producto():
    id_producto = generar_ids()
    categoria = random.choice(list(PRODUCTOS_POR_CATEGORIAS.keys()))
    nombre = random.choice(PRODUCTOS_POR_CATEGORIAS[categoria])
    rango_precio = PRECIO_POR_CATEGORIA[categoria]
    precio = round(random.uniform(rango_precio[0], rango_precio[1]), 2)
    stock = random.randint(1, 100)
    rate = round(random.uniform(1.0, 10.0), 1)

    return Productos(id_producto, nombre, precio, categoria, stock, rate)



