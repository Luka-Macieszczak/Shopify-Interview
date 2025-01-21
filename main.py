import math

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
    
    def get_closest_warehouse(self, x, y):
        min_dist, idx = float('inf'), -1
        for i, warehouse in enumerate(self.warehouses):
            wx, wy = warehouse.coordinates
            dist = math.sqrt((x - wx)**2 + (y - wy)**2)
            if dist < min_dist:
                min_dist = dist
                idx = i
        
        return self.warehouses[idx]
    
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
    
    def closest_to_buyer(self, buyer, query):
        x, y = buyer.coordinates
        return self.product.get_closest_warehouse(x, y)
    
    def print_data(self):
        self.product.print_data()
        



def main():
    warehouses = [Warehouse('Ottawa', 'Canada', [2, 2], 5) for _ in range(5)]
    merchant = Merchant('snowboards', warehouses)

    warehouses[2].coordinates = [1, 1]
    warehouses[2].city = "Toronto"

    buyer = Buyer("Luka", "Ottawa", "Canada", [1, 1])
    query = Query('snowboards', 3)
    # for warehouse in warehouses:
    #     warehouse.print_data()
    # merchant.print_data()

    # for warehouse in merchant.ship_within_country(buyer, query):
    #     warehouse.print_data()

    merchant.closest_to_buyer(buyer, query).print_data()

if __name__ == '__main__':
    main()
    

