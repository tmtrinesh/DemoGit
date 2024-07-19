ItemsInCart = 0
# 2 items ll be added to cart
if ItemsInCart !=2: #raise exception("product cart count not matchinh")
    pass
assert (ItemsInCart == 0)

#try,except
try:
    with open('filelog.txt','r') as reader:
        reader.read()

except:
    print("somehow I reached except  block due to failure in try block ")

try:
    with open('filelog.txt','r') as reader:
        reader.read()

except Exception as e:
    print(e)

finally:

    print("code terminated")