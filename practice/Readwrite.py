file = open('test.txt')
#Read all the contents of file
#print(file.read(2)) # to read n number of chars bys passing parameters


#print(file.readline())# read 1st line
#print(file.readline())#read 2nd line

#Interview question
#print line by line using readline method
#line = file.readline()
#while line != "":
#    print(line)
#    line = file.readline()

# Read line method
#print(file.readlines()) # all the elements ll be printed in the form of list

values = ['azx', 'bqw', 'cat', 'dog', 'elephant']
for line in file.readlines():
    print(line)





file.close()