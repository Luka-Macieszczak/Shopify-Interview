class Warehouse:
    def __init__(self, city, country, coordinates, stock):
        self.city = city
        self.country = country
        self.coordinates = coordinates
        self.stock = stock
        pass

    def print_data(self):
        print("city: ", self.city)
        print("country: ", self.country)
        print("coordinate: ", self.coordinates)
        print("stock: ", self.stock)

class Product:
    def __init__(self, name, warehouses=[]):
        self.warehouses = warehouses
        self.name = name

    def get_warehouses_in_country(self, country):
        ret = []
        for warehouse in self.warehouses:
            if warehouse.country == country:
                ret.append(warehouse)
        return ret
    
    def print_data(self):
        print("name: ", self.name)
        for warehouse in self.warehouses:
            warehouse.print_data()
    

class Buyer:
    def __init__(self, name, city, country, coordinates):
        self.name = name
        self.city = city
        self.country = country
        self.coordinates = coordinates

    def print_data(self):
        print("name: ", self.name)
        print("city: ", self.city)
        print("country: ", self.country)
        print("coordinate: ", self.coordinates)

class Query:
    def __init__(self, product_name, quantity):
        self.product_name = product_name
        self.quantity = quantity
    

class Merchant:
    def __init__(self, name, warehouses):
        self.product = Product(name, warehouses)
 
    def ship_within_country(self, buyer, query):
        country = buyer.country
        return self.product.get_warehouses_in_country(country)
    
    def print_data(self):
        self.product.print_data()
        



def main():
    warehouses = [Warehouse('Ottawa', 'Canada', [1, 1], 5) for _ in range(5)]
    merchant = Merchant('snowboards', warehouses)

    buyer = Buyer("Luka", "Ottawa", "Canada", [1, 1])
    query = Query('snowboards', 3)
    # for warehouse in warehouses:
    #     warehouse.print_data()
    # merchant.print_data()

    for warehouse in merchant.ship_within_country(buyer, query):
        warehouse.print_data()

if __name__ == '__main__':
    main()
    

