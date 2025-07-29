class Productos:
    def __init__(self, id_product, nombre, precio, categoria, stock, rate):
        self.id_product = id_product
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.stock = stock
        self.rate = rate
        
    def __str__(self):
        return (
            f"ID: {self.id_product} - "
            f"Nombre: {self.nombre} - "
            f"Categoría: {self.categoria} - "
            f"Precio: {self.precio}$ - "
            f"Stock: {self.stock} - "
            f"Rating: {self.rate}/10"
        )