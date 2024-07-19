class Computer:
    def __init__(self):
        print("init ")

    def config(self):
        print("i3,8gb,1TB")

com1 = Computer() # object creation
com2 = Computer()

Computer.config(com1)
Computer.config(com2)

com1.config()  #we are calling object by class
com2.config()