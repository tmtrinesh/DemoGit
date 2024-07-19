class InvalidData(Exception):
    pass

marks=int(input("Enter marks for student"))
try:
    if marks<0 or marks>100:
        raise InvalidData
except InvalidData:
    print("Marks should be between 0 and 100")
