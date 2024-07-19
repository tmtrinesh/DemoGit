class Base:
    def display(self):
        print("Base class")

class Base1:
    def bdisplay(self):
        print("Base class1")

class Child(Base,Base1):
    def show(self):
        print("Child class")

c=Child()
c.bdisplay()
c.display()
c.show()
