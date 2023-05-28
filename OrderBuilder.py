class OrderBuilder:
    def __init__(self, customer_name, customer_phone, customer_address, customer_payment, customer_order_type):
        self.customer_name = customer_name
        self.customer_phone = customer_phone
        self.customer_address = customer_address
        self.customer_payment = customer_payment
        self.customer_order_type = customer_order_type
        self.customer_surname = "bkn"
        self.customer_cart_no = 0
        self.customer_cart_month = 10
        self.customer_cart_year = 28
        self.customer_cart_cvv = 888
        self.next_handler = None
        self.customer_id = 1

    def set_next_handler(self, handler):
        self.next_handler = handler

    def create_order(self):
        if self.next_handler is not None:
            return self.next_handler.handle(self)
        else:
            raise Exception("No handler set for order creation")


class StockControl:
    def check_stock(self, order_builder):
        print("ürün stokta bulunmaktadır")


class PaymentBuilder:
    def __init__(self, customer_name, customer_surname, customer_cart_no, customer_cart_month,
                 customer_cart_year, customer_cart_cvv):
        self.customer_name = customer_name
        self.customer_surname = customer_surname
        self.customer_cart_no = customer_cart_no
        self.customer_cart_month = customer_cart_month
        self.customer_cart_year = customer_cart_year
        self.customer_cart_cvv = customer_cart_cvv
        self.next_handler = True

    def set_next_handler(self, handler):
        self.next_handler = handler

    def pay_complete(self):
        if self.next_handler is not None:
            return True
        else:
            raise Exception("No handler set for payment completion")


class OrderTransit:
    def __init__(self, customer_id, customer_name, customer_surname, customer_address):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.customer_surname = customer_surname
        self.customer_address = customer_address
        self.next_handler = True

    def set_next_handler(self, handler):
        self.next_handler = handler

    def transit(self):
        if self.next_handler is not None:
            return self.next_handler
        else:
            raise Exception("No handler set for order transit")


class ChainHandler:
    def __init__(self):
        self.next_handler = None

    def set_next_handler(self, handler):
        self.next_handler = handler

    def handle(self, obj):
        raise NotImplementedError()


class StockControlHandler(ChainHandler):
    def handle(self, obj):
        stock_control = StockControl()
        stock_control.check_stock(obj)
        if self.next_handler is not None:
            return self.next_handler.handle(obj)
        else:
            return "Order created"


class PaymentHandler(ChainHandler):
    def handle(self, obj):
        payment_builder = PaymentBuilder(obj.customer_name, obj.customer_surname, obj.customer_cart_no,
                                         obj.customer_cart_month, obj.customer_cart_year, obj.customer_cart_cvv)
        payment_builder.pay_complete()
        if self.next_handler is not None:

            return self.next_handler.handle(obj)
        else:
            return "Ödeme tamamlandı"


class OrderTransitHandler(ChainHandler):
    def handle(self, obj):

        order_transit = OrderTransit(obj.customer_id, obj.customer_name, obj.customer_surname, obj.customer_address)
        print("Sipariş kargoya verildi.")
        return order_transit.transit()


# Kullanım örneği
order_builder = OrderBuilder("John Doe", "123456", "123 Main St", "Credit Card", "Phone")
stock_handler = StockControlHandler()
payment_handler = PaymentHandler()
transit_handler = OrderTransitHandler()

order_builder.set_next_handler(stock_handler)
stock_handler.set_next_handler(payment_handler)
payment_handler.set_next_handler(transit_handler)

result = order_builder.create_order()
