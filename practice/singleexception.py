a = int(input("Enter value of a:"))
b = int(input("Enter value of b:"))
l=[10,20,30,40,50]

try:
    c= a/b
    print(c)
    print(l[5])
except Exception as e:
    print(e)
