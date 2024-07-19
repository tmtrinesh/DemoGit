a = int(input("Enter value of a:"))
b = int(input("Enter value of b:"))

try:
    if b==0:
        raise ZeroDivisionError("divided by Zero") # you can write exception raised instead
    c= a/b
    print(c)
except ZeroDivisionError as e:
    print(e)


marks = int(input("Enter marks"))
try:
    if marks<0 or marks>100:
        raise Exception("marks should be in between 0 and 100")
    print("marks = ",marks)
except Exception as e:
    print(e)
