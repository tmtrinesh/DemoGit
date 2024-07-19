#method name should be same
#No of arguements should b same
class Father:
    def transport(self):
        print("Cycle")


class Son(Father):
    def transport(self):
        print("Bike")



obj =Son()
obj.transport()
#no of parameters also should be same

