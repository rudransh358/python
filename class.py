class parent(object):
    def m1(self):
        print("parent class m1 method")
        self.a = 10

class child(parent):  
    def m2(self):
        print("child class m2 method")
        self.b = 20

cobj = child()     
cobj.m1()           
cobj.m2()           
print(cobj.a, cobj.b)
