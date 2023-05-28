from abc import ABC, abstractmethod

# IPowerCable soyut sınıfı (Abstract Class)
class IPowerCable(ABC):
    @abstractmethod
    def createCablePhone(self):
        pass

    @abstractmethod
    def createCableTablet(self):
        pass

    @abstractmethod
    def createCablePC(self):
        pass

# TypeCCable sınıfı, IPowerCable arayüzünü uygular
class TypeCCable(IPowerCable):
    def createCablePhone(self):
        return Phone("Type-C")

    def createCableTablet(self):
        return Tablet("Type-C")

    def createCablePC(self):
        return PC("Type-C")

# TypeC13Cable sınıfı, IPowerCable arayüzünü uygular
class TypeC13Cable(IPowerCable):
    def createCablePhone(self):
        return Phone("Type-C 13")

    def createCableTablet(self):
        return Tablet("Type-C 13")

    def createCablePC(self):
        return PC("Type-C 13")

# TypeLightningCable sınıfı, IPowerCable arayüzünü uygular
class TypeLightningCable(IPowerCable):
    def createCablePhone(self):
        return Phone("Lightning")

    def createCableTablet(self):
        return Tablet("Lightning")

    def createCablePC(self):
        return PC("Lightning")

# Phone sınıfı
class Phone:
    def __init__(self, cable_type):
        self.cable_type = cable_type

    def __str__(self):
        return f"Phone - Cable Type: {self.cable_type}"

# Tablet sınıfı
class Tablet:
    def __init__(self, cable_type):
        self.cable_type = cable_type

    def __str__(self):
        return f"Tablet - Cable Type: {self.cable_type}"

# PC sınıfı
class PC:
    def __init__(self, cable_type):
        self.cable_type = cable_type

    def __str__(self):
        return f"PC - Cable Type: {self.cable_type}"

# Abstract Factory kullanım örneği
def createDevices(factory):
    phone = factory.createCablePhone()
    tablet = factory.createCableTablet()
    pc = factory.createCablePC()
    print(phone)
    print(tablet)
    print(pc)

# TypeCCable kullanım örneği
type_c_factory = TypeCCable()
createDevices(type_c_factory)

# TypeC13Cable kullanım örneği
type_c13_factory = TypeC13Cable()
createDevices(type_c13_factory)

# TypeLightningCable kullanım örneği
type_lightning_factory = TypeLightningCable()
createDevices(type_lightning_factory)
