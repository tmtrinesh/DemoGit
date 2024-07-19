
import numpy
c = numpy.cbrt([27])
print(c)

txt = "basketball,ba,ball,bask,sketba,basket"
txt1 = "basketball", "aske,bal,bas,tbal"

print(txt[6:])

print(txt1[1])

word = "welcome to jungle"
x = word.split()
print(x)
if x[2] == "jungle":
    print("test passed")
else:
    print("test failed")

fruit = "apple#banana#cherry#orange"
y = fruit.split("#", 3)
print(y)
print(y[1])
