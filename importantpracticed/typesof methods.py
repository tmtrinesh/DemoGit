class Student:

    school = "Telusko"
    def __init__(self,m1,m2,m3):
        self.m1= m1
        self.m2 = m2
        self.m3 =m3

    def avg(self):
        return(self.m1 + self.m2 + self.m3)/3


    def get_m1(self):
        return self.m1

    def set_m1(self,value):
        self.m1 = value


    @classmethod  #defining decorator printing output by class name
    def info(cls):
        return cls.school

    @staticmethod
    def info():
        print("This is Student class.. in abc module")

s1 = Student(34,21,36)
s2 = Student(36, 24,28)


print(s1.avg())
print(s2.avg())
print(s1.info())
print(Student.info()) #getting output by classname


Student.info()


