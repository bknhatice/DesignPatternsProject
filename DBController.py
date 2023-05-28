import sqlite3

class DBController:
    __instance = None

    def __init__(self):
        if DBController.__instance is not None:
            raise Exception("Singleton class. Use getInstance() to get the instance.")
        DBController.__instance = self

        # Veritabanı bağlantısı ve diğer başlangıç işlemleri
        self.connection = None
        self.connected = False

    @staticmethod
    def getInstance():
        if DBController.__instance is None:
            DBController()
        return DBController.__instance

    def connect_to_database(self):
        connection = sqlite3.connect("database.db")
        return connection

    def connect(self, connection_string):
        # Veritabanına bağlantı kurma işlemleri
        # connection_string kullanarak bağlantı sağlanır
        self.connection = self.connect_to_database()
        self.connected = True

    def execute_database_query(self, connection, query):
        '''cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall() '''
        return "3" # örnek olarak verilmiştir.

    def execute_query(self, query):
        if not self.connected:
            raise Exception("Not connected to the database.")

        # Veritabanına sorgu gönderme ve sonuçları alma işlemleri
        result = self.execute_database_query(self.connection, query)
        if int(result) > 0:
            print("Ürün stokta bulunmaktadır.")
        else:
            print("ürün stokta yoktur")
        return result

# Kullanım örneği
db_controller = DBController.getInstance()
db_controller.connect("connection_string")

query = "SELECT * FROM Orders"
result = db_controller.execute_query(query)
print(result)
