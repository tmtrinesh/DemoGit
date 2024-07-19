class Computer:
    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram


    def config(self):
        print("Config is",self.cpu,self.ram)

com1 = Computer('i5',16) # object creation
com2 = Computer('reyzon 3',8)

#Computer.config(com1)#alternate method
#Computer.config(com2)

com1.config()  #we are calling object by class
com2.config()
