class Warehouse:
    def __init__(self, city, country, coordinates, stock):
        self.city = city
        self.country = country
        self.coordinates = coordinates
        self.stock = stock
        pass

class Product:
    def __init__(self, name, warehouses=[]):
        self.warehouses = warehouses
        self.name = name

class Buyer:
    def __init__(self, name, city, country, coordinates):
        self.name = name
        self.city = city
        self.country = country
        self.coordinates = coordinates

class Query:
    def __init__(self, product_name, quantity):
        self.product_name = product_name
        self.quantity = quantity

class Merchant:
    def __init__(self, name, warehouses):
        self.product = Product(name, warehouses)

    

