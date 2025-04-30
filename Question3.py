class Device:
    def __init__(self,device_name,brand,battery_life,price):
        self.__device_name = device_name
        self.__brand = brand
        self.__battery_life = battery_life
        self.__price = price
    def get_device_name(self):
        return self.__device_name
    def get_brand(self):
        return self.__brand
    def get_battery_life(self):
        return self.__battery_life
    def get_price(self):
        return self.__price
    def print_details(self):
        print(self.__device_name, self.__brand, self.__battery_life, self.__price)

class Phone(Device):
    def __init__(self,device_name,brand,battery_life,price,storage):
        super(device_name,brand,battery_life,price)
        self.__storage = storage

    def get_storage(self):
        return self.__storage
    def print_details(self):
        print(self.__device_name, self.__brand, self.__battery_life, self.__price, self.__storage)  

class Laptop(Device):
    def __init__(self,device_name,brand,battery_life,price,ram):
        super(device_name,brand,battery_life,price)
        self.__ram = ram

    def get_ram(self):
        return self.__ram
    def print_details(self):
        print(self.__device_name, self.__brand, self.__battery_life, self.__price, self.__ram)  

class Tablet(Device):
    def __init__(self,device_name,brand,battery_life,price,screen_size):
        super(device_name,brand,battery_life,price)
        self.__screen_size = screen_size

    def get_screen_size(self):
        return self.__screen_size
    def print_details(self):
        print(self.__device_name, self.__brand, self.__battery_life, self.__price, self.__screen_size)



def ReadDeviceData():
    global DeviceArray
    DeviceArray = [Device("","",0,0.0)]
    file = open("Devices.txt", 'r')
    line = file.readline().strip()

    DeviceType =line.split(",")
    DeviceName =line.split(",")
    Brand = line.split(",")
    BatteryLife = line.split(",")
    Price = line.split(",")
    ExtraAttribute = line.split(",")

    if DeviceType == "Tablet":
        New =Tablet(DeviceType,DeviceName,Brand,BatteryLife,Price,ExtraAttribute)
    if DeviceType == "Laptop":
        New =Laptop(DeviceType,DeviceName,Brand,BatteryLife,Price,ExtraAttribute)
    if DeviceType == "Phone":
        New =Phone(DeviceType,DeviceName,Brand,BatteryLife,Price,ExtraAttribute)


    DeviceArray.append(New)
    return DeviceArray

def PrintDevices(Array):
    for i in range(len(Array)):
        print(Array[i].get_device_name(),Array[i].get_brand(),Array[i].get_battery_life(),Array[i].get_price)
            

array = ReadDeviceData()
PrintDevices()

