class student:
    rno=123  #instance variables
    name="abc"  #instance variables
    branch="cse"   #instance variables
    def read(self):
        rollno=345  #local variable
        print("rollno",rollno)
        print("Instance variable=",self.rno)
        print("reading")
    def write(self):
        print("writing...")

abc=student()
print("rno=",abc.rno)
print("name=",abc.name)
print("branch=",abc.branch)
abc.read()
abc.write()
