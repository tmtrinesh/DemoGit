a,b=15,25
class MyClass:
    a,b = 10,20

    def add(self,a,b):
        print(a+b)
        print(self.a + self.b)
        print(globals()['a']+globals()['b'])

mc =MyClass()
mc.add(100,200)
