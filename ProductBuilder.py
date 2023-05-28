import PowerCable
from PowerCable import IPowerCable
# PCBuilder sınıfı
class PCBuilder:
    def __init__(self):
        self.screen_size = None
        self.cpu_speed = None
        self.gpu = None
        self.power = None

    def buildScreen(self, screen_size):
        self.screen_size = screen_size
        return self

    def buildCPU(self, cpu_speed):
        self.cpu_speed = cpu_speed
        return self

    def buildGPU(self, gpu):
        self.gpu = gpu
        return self

    def buildPower(self, power):
        self.power = power
        return self

    def build(self):
        return PC(self.screen_size, self.cpu_speed, self.gpu, self.power)

# TabletBuilder sınıfı
class TabletBuilder:
    def __init__(self):
        self.screen_size = None
        self.cpu_speed = None
        self.camera_type = None
        self.os = None

    def buildScreen(self, screen_size):
        self.screen_size = screen_size
        return self

    def buildCPU(self, cpu_speed):
        self.cpu_speed = cpu_speed
        return self

    def buildCamera(self, camera_type):
        self.camera_type = camera_type
        return self

    def buildOS(self, os):
        self.os = os
        return self

    def build(self):
        return Tablet(self.screen_size, self.cpu_speed, self.camera_type, self.os)

# PhoneBuilder sınıfı
class PhoneBuilder:
    def __init__(self):
        self.screen_size = None
        self.color = None
        self.camera_type = None
        self.os = None

    def buildScreen(self, screen_size):
        self.screen_size = screen_size
        return self

    def buildColor(self, color):
        self.color = color
        return self

    def buildCamera(self, camera_type):
        self.camera_type = camera_type
        return self

    def buildOS(self, os):
        self.os = os
        return self

    def build(self):
        return Phone(self.screen_size, self.color, self.camera_type, self.os)

# PC sınıfı
class PC:
    def __init__(self, screen_size, cpu_speed, gpu, power):
        self.screen_size = screen_size
        self.cpu_speed = cpu_speed
        self.gpu = gpu
        self.power = power
        self.power_cable = PowerCable.IPowerCable.createCablePC()

    def __str__(self):
        # PCBuilder kullanım örneği
        pc_builder = PCBuilder()
        pc = pc_builder.buildScreen(17.3).buildCPU("3.5 GHz").buildGPU(True).buildPower(500).build()
        print(pc)
        return f"PC - Screen Size: {self.screen_size}, CPU Speed: {self.cpu_speed}, GPU: {self.gpu}, Power: {self.power}"

# Tablet sınıfı
class Tablet:
    def __init__(self, screen_size, cpu_speed, camera_type, os):
        self.screen_size = screen_size
        self.cpu_speed = cpu_speed
        self.camera_type = camera_type
        self.os = os
        self.power_cable = PowerCable.IPowerCable.createCableTablet()

    def __str__(self):
        # TabletBuilder
        tablet_builder = TabletBuilder()
        tablet = tablet_builder.buildScreen(17.3).buildCPU("3.5 GHz").buildCamera(True).buildOS("mac").build()
        print(tablet)
        return f"Tablet - Screen Size: {self.screen_size}, CPU Speed: {self.cpu_speed}, Camera Type: {self.camera_type}, OS: {self.os}"

# Phone sınıfı
class Phone:
    def __init__(self, screen_size, color, camera_type, os):
        self.screen_size = screen_size
        self.color = color
        self.camera_type = camera_type
        self.os = os
        self.power_cable = PowerCable.IPowerCable.createCablePhone()

    def __str__(self):
        phone_builder = PhoneBuilder()
        phone = phone_builder.buildScreen(17.3).buildColor("pink").buildCamera(True).buildOS("android").build()
        print(phone)
        return f"Phone - Screen Size: {self.screen_size}, Color: {self.color}, Camera Type: {self.camera_type}, OS: {self.os}"

pc_builder = PCBuilder()
pc = pc_builder.buildScreen(17.3).buildCPU("3.5 GHz").buildGPU(True).buildPower(500).build()
print(pc)