class Encap:
    a=10;  #private variable
    def display(self):  #private variable & private method cant be accesed outside the class
        print("Welcome")
        print(self.a)  #private variable inside the class

obj=Encap()
print(obj.a)
obj.display()

