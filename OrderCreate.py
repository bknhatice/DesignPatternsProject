import OrderBuilder

# OrderCreate sınıfı
class OrderCreate:
    def create_order(self, customer_name, customer_phone, customer_address, customer_payment, customer_order_type):
        order_factory = OrderFactory()
        order_factory.create_order(customer_name, customer_phone, customer_address, customer_payment, customer_order_type)

# IProduct arayüzü
class IProduct:
    def create_product(self, screen_size, cpu, os, color, price, product_id):
        pass
# OrderFactory sınıfı
class OrderFactory:
    def create_order(self, customer_name, customer_phone, customer_address, customer_payment, customer_order_type):
        product = self.create_product(customer_order_type)
        if product:
            # Sipariş oluşturma işlemleri burada gerçekleştirilir
            print("Sipariş oluşturuldu:", customer_name, customer_phone, customer_address, customer_payment)
            print("Ürün bilgileri:", product)
        else:
            print("Geçersiz sipariş türü.")

    def create_product(self, product_type):
        if product_type == "Example Type":
            product = ExampleProduct()
            return product.create_product(15, "Intel i5", "Windows 10", "Black", 1000, 123)
        return None

# ExampleProduct sınıfı
class ExampleProduct(IProduct):
    def create_product(self, screen_size, cpu, os, color, price, product_id):
        # Ürün oluşturma işlemleri burada gerçekleştirilir
        return {
            "Screen Size": screen_size,
            "CPU": cpu,
            "OS": os,
            "Color": color,
            "Price": price,
            "Product ID": product_id
        }
# main() fonksiyonu
def main():
    order_builder = OrderBuilder()
    order_builder.customer_order_type = "Example Type"
    order_builder.create_order()

if __name__ == "__main__":
    main()