class Base:
    def display(self):
        print("Parent1")

class Child(Base):
    def show(self):
        print("Child")
class Child1(Base):
    def cdisplay(self):
        print("Child1")

c1 = Child()
c1.display()
c1.show()

c2=Child1()
c2.display()
c2.cdisplay()