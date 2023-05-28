# StockControl sınıfı
class StockControl:
    def __init__(self):
        self.__product_serial_no = 123
        self.__product_name = "Example Product"
        self.__product_type = "Example Type"
        self.__product_count = 10

    def check_stock(self, order_type):
        # Sipariş türüne göre stok kontrolü yapılır
        if order_type == self.__product_type and self.__product_count > 0:
            self.__product_count -= 1
            return True
        return False
