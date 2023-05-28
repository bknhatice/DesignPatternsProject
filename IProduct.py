from abc import ABC, abstractmethod


# IProduct arayüzü
class IProduct(ABC):
    @abstractmethod
    def getProduct(self):
        pass

    @abstractmethod
    def clone(self):
        pass


# Phone sınıfı
class Phone(IProduct):
    def __init__(self, screen_size, cpu, os, color, price):
        self.screen_size = screen_size
        self.cpu = cpu
        self.os = os
        self.color = color
        self.price = price

    def getProduct(self):
        return "Phone"

    def clone(self):
        return Phone(self.screen_size, self.cpu, self.os, self.color, self.price)


# Tablet sınıfı
class Tablet(IProduct):
    def __init__(self, screen_size, cpu, os, color, price):
        self.screen_size = screen_size
        self.cpu = cpu
        self.os = os
        self.color = color
        self.price = price

    def getProduct(self):
        return "Tablet"

    def clone(self):
        return Tablet(self.screen_size, self.cpu, self.os, self.color, self.price)


# PC sınıfı
class PC(IProduct):
    def __init__(self, screen_size, cpu, os, color, price):
        self.screen_size = screen_size
        self.cpu = cpu
        self.os = os
        self.color = color
        self.price = price

    def getProduct(self):
        return "PC"

    def clone(self):
        return PC(self.screen_size, self.cpu, self.os, self.color, self.price)


# ProductFactory sınıfı
class ProductFactory:
    def __init__(self):
        self.__product_cache = {}

    def create_product(self, screen_size, cpu, os, color, price, product_id):
        cache_key = f"{screen_size}-{cpu}-{os}-{color}-{price}-{product_id}"
        if cache_key in self.__product_cache:
            return self.__product_cache[cache_key].clone()

        product = None
        if product_id == 1:
            product = Phone(screen_size, cpu, os, color, price)
        elif product_id == 2:
            product = Tablet(screen_size, cpu, os, color, price)
        elif product_id == 3:
            product = PC(screen_size, cpu, os, color, price)

        if product:
            self.__product_cache[cache_key] = product
            return product.clone()

        return None


# main() fonksiyonu
def main():
    product_factory = ProductFactory()

    product1 = product_factory.create_product(5.5, "Snapdragon 855", "Android", "Black", 999, 1)
    if product1:
        print("Product Type:", product1.getProduct())

    product2 = product_factory.create_product(10.1, "Apple A14", "iOS", "Silver", 1499, 2)
    if product2:
        print("Product Type:", product2.getProduct())

    product3 = product_factory.create_product(15.6, "Intel Core i7", "Windows 10", "Black", 1999, 3)
    if product3:
        print("Product Type:", product3.getProduct())


if __name__ == "__main__":
    main()
