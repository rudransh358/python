class parent(object):
    def func(self):
        print("this is a function 1")
class child(parent):
    def func2(self):
        print("this is a function 2")
class child2(child):
    def func3(self):
        print("this is a function 3")
ob = child2()
ob.func()
ob.func2()
ob.func3()