from abc import ABC,abstractmethod
class AbstractDemo(ABC):  #abstract class
    @abstractmethod     #abstract method
    def display(self):
        None
    @abstractmethod
    def show(self):
        None


class Demo(AbstractDemo): #abstract class
    def display(self):
        print("Abstract method")

    def show(self):
        print("Show method")
class Demo1(AbstractDemo):  #Concrete class
    def show(self):
        print("Show method")
    def display(self):
        print("dispaly method")


obj=Demo1()
obj.display()
obj.show()


# Abstract class are those which have abstract methods
#Abstract method is a method with declarion but not with defination