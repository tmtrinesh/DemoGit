
class Moverload:
    def display(self,a=None,b=None):
        print(a,b)

obj=Moverload()
obj.display() #1st fun cal
obj.display(10) #assigned value to a &  2nd fun cal not assigned
obj.display(10,20) #assignd value to both a b


