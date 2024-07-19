a= 10  #global variable
def display():
    a=100
    def show():
        nonlocal a
        a=a+1
        print("Inside show",a)
    show()
    print("Inside display:",a)
display()
print("Outside:",a)
#local variable if ther is no value assigned to a in local it ll take global value
#with out assigning local var if u perform operation like a = a+10,it ll give unbound localerror
# or give global a inside func so that it ll take gobal value