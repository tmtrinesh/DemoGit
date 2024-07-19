class Base:
    def display(self):
        print("Parent1")

class Child(Base):
    def show(self):
        print("Child")
c1 = Base()
c1.display()


