class Computer:
    def __init__(self):
        self.name = "Naveen"
        self.age = 20


   # def update(self):
    #    self.age = 30

    def compare(self,other):
        if self.age == other.age:
            return True
        else:
            return False





c1 = Computer()
c1.age = 30
c2 = Computer()

if c1.compare(c2):
    print("they are same")
else:
    print("they are different")

c1.name = "Navya"


#c1.update()

print(c1.name)
print(c2.name)
print(c1.age)
print(c2.age)
