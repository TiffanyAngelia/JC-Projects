class Device:
    def __init__(self,device_name,brand,battery_life,price):
        self.__device_name = device_name #STRING
        self.__brand = brand #STRING
        self.__battery_life = battery_life #INTEGER
        self.__price = price #FLOAT

    def get_device_name(self):
        return self.__device_name
    def get_brand(self):
        return self.__brand
    def get_battery_life(self):
        return self.__battery_life
    def get_price(self):
        return self.__price
    def print_details(self):
        print(f"Device name: {self.get_device_name()}, Brand: {self.get_brand()}, Battery Life: {self.get_battery_life()}, Price: {self.get_price()}")

class Phone(Device):
    def __init__(self,device_name,brand,battery_life,price,storage):
        super().__init__(device_name,brand,battery_life,price) #DO NOT PUT SELF
        self.__storage = storage

    def get_storage(self):
        return self.__storage
    def print_details(self):
        print(f"Device name: {self.get_device_name()}, Brand: {self.get_brand()}, Battery Life: {self.get_battery_life()}, Price: {self.get_price()}, Storage: {self.get_storage()}")

class Laptop(Device):
    def __init__(self,device_name,brand,battery_life,price,ram):
        super().__init__(device_name,brand,battery_life,price)
        self.__ram = ram #INTEGER
    
    def get_ram(self):
        return self.__ram
    def print_details(self):
        print(f"Device name: {self.get_device_name()}, Brand: {self.get_brand()}, Battery Life: {self.get_battery_life()}, Price: {self.get_price()}, Ram: {self.get_ram()}")

class Tablet(Device):
    def __init__(self,device_name,brand,battery_life,price,screen_size):
        super().__init__(device_name,brand,battery_life,price) 
        self.__screen_size = screen_size #FLOAT
    
    def get_screen_size(self):
        return self.__screen_size
    def print_details(self):
        print(f"Device name: {self.get_device_name()}, Brand: {self.get_brand()}, Battery Life: {self.get_battery_life()}, Price: {self.get_price()}, Screen Size: {self.get_screen_size()}")


def ReadDeviceData():
    try:
        DeviceArray = []
        file = open("Past Year Papers/Prelim25/Devices.txt", 'r')

        for lines in file:

            ItemArray = lines.strip().split(',') #DO NOT MAKE ItemArray = [] !!! 
            if ItemArray[0] == "Phone":
                DeviceArray.append(Phone(ItemArray[1], ItemArray[2], int(ItemArray[3]), float(ItemArray[4]), int(ItemArray[5])))
            elif ItemArray[0] == "Laptop":
                DeviceArray.append(Laptop(ItemArray[1], ItemArray[2], int(ItemArray[3]), float(ItemArray[4]), int(ItemArray[5])))
            elif ItemArray[0] == "Tablet":
                DeviceArray.append(Tablet(ItemArray[1], ItemArray[2], int(ItemArray[3]), float(ItemArray[4]), float(ItemArray[5])))
        file.close()
        return DeviceArray
    
    except FileNotFoundError:
        print("File not found")

def PrintDevices(ArrayObj):
    for obj in ArrayObj:
        obj.print_details()

def ChooseDevice(ArrayObj):
    UserBudget = float(input("Enter your budget: "))
    UserBrand = input("Enter the brand you prefer: ")
    UserBattery = int(input("Enter the minimum battery life you prefer: "))
    Options = []

    for obj in ArrayObj:
        if obj.get_brand() == UserBrand and obj.get_battery_life() >= UserBattery and obj.get_price() <= UserBudget:
            Options.append(obj)
    return Options

DevicesArray = ReadDeviceData()
PrintDevices(DevicesArray)

DeviceOptions = ChooseDevice(DevicesArray)
if DeviceOptions == []:
    print("No devices meet the requirements! ")
else: 
    PrintDevices(DeviceOptions)