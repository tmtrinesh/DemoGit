#COMMAND LINE ARGYEMENTS
#Another way to accept the inputs other than input()
#Inputs ll be passed to the program as an arguements from command prompt
#sys module
# all commamds prompts given forms a list as argv
#argv is list "sys.argv"
# Elements og argv can be accessed using INDEX
#INDEX starts from 0
#Alaways sys.argv[0] ---Filename
        # sys.argv[1]  arguements
import  sys
print(sys.argv)
print(len(sys.argv)) # --length and arguements including filename
for i in range(0,len(sys.argv)):
    print("Arguement-",i,":",sys.argv[i])
#1.write program
#2.save with .py extension
#3.open command prompt
#4.change the path to where the program is being saved
#py filename.py arg1 arg2 arg3...



