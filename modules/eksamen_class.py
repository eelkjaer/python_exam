import datetime

class Computer:

    def __init__(self, model='', screen=0, ram=0, ssd=0, price=0, url='', brand='', cpu='', processor=''):
        self.brand = brand
        self.model = model
        self.cpu = cpu
        self.processor = processor
        self.ram = ram
        self.ssd = ssd
        self.screen = screen
        self.price = price
        self.date = str(datetime.date.today().day) + "-" + str(datetime.date.today().month) + "-" + str(
            datetime.date.today().year)
        self.url = url

    def __str__(self):
        return "Brand: {}, model: {}, cpu: {}, processor: {}, ram: {}, ssd: {}, screen: {}, price: {}, date: {}, url: {}".format(
            self.brand, self.model, self.cpu, self.processor, self.ram, self.ssd, self.screen, self.price, self.date,
            self.url)

    def __repr__(self):
        return self.__str__()

    def setBrand(self, brand):
        self.brand = brand

    def setCpu(self, cpu):
        self.cpu = cpu

    def setProcessor(self, processor):
        self.processor = processor
