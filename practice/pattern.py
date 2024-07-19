for i in range(4):
    for j in range(i+1):
        print("#",end="")

    print()


print("Hello \n World")
print("Hello \t world")
print("\nTrinesh\ngowda")


def fact(num):
    if (num>1):
        num = num * fact(num-1)
    return num
print(fact(5))


cube = lambda x : x*x*x
print(cube(6))

class pop:
    pass
p1 = pop()

s = set("python")
print(s)

s1 = str("python")
print(s1[2::])
print(s1[::-1])
print(s1)