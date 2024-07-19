#self keyword is mandatory for calling variable names into method
#instance and class variables have whole different
#constructor nme should be __init__
#new keyword is not required when you create obj

#comments not required if u dont knoe other lang
class Calculator:
    num = 100 #class variables
#default constructor ll be caleed
#what are parametes we call in class should call in constructor othwerwose it ll throw error

    def __init__(self,a,b):
        self.firstnumber = a  # inatance variables
        self.secondnumber = b  # inatance variables
        print("I am called automatically when object is created")

#basically functions when used as cclass will called aas methods
    def getData(self):
        print("I am now executing  as methods in class")

    def summation(self):
        return self.firstnumber + self.secondnumber + Calculator.num
        print("")


obj = Calculator(2,3) #syntax to create object in python
obj.getData()
print(obj.summation())

obj1 = Calculator(4,5) #syntax to create object in python
obj1.getData()
print(obj1.summation())


