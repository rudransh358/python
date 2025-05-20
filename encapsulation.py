class Employee:
    def __init__(self):
        self.__name = "Rudransh"
        self.__addr = "Bhubaneswar"
        self.__sal = 5000

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setAddr(self, addr):
        self.__addr = addr

    def getAddr(self):
        return self.__addr

    def setSal(self, sal):
        self.__sal = sal

    def getSal(self):
        return self.__sal


e = Employee()

print(e.getName())

e.setName("Rudransh Singh")
print(e.getName())

print(e.getAddr())

e.setAddr("Cuttack")
print(e.getAddr())

print(e.getSal())

e.setSal(100000)
print(e.getSal())
