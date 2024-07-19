# 1.Open()
#Syntax :file_object=open("filename.txt","access mode")
#file_object is called as file pointer which points to the content of file
#Access Modes

#r - read mode--file is opened only for reading the content
#file pointer points at the beginning of the file
#file should exixst before opening in read mode
fp=open("mphasis.txt","r")

#w --write mode--If the file exists then file is opened and pointer points at  beginning & data ll overwritten
#if the file doesnt exist then new file ll be created with given file name
fp=("abc.txt","w")

#a--append mode-only to append and write the data into the file
#if file exist --file pointer points at the end of the content file
#if file doesnt exists new file ll be created  and file pointer points at beginning
fp=("abc.txt","a")

# r+  it is for reading & writing
# w+ it is for reading & writing
# a+ it is for reading & appending
# all these for text files


#########################################################################
# these are for binary files
#rb  reading
#wb  writing
#ab appending

# rb+  it is for reading & writing
# wb+ it is for reading & writing
# ab+ it is for reading & appending

# append mode file pointer at the end of the content
# write mode  file pointer at the beginning
#read mode  file pointer in the beginning
#file_object.close() --ll close every opened file

#reading --'r'
#writing --'w' ,'a'
# for 'w' mode--if file exists --contnts ll be overwritten
#if file doesnt exist--new file ll be created
#'a' mode if file exists --pointer points at the end of content
#file doent exists --new file ll be created





