list = [[1,2],[3,4],[5,6],[7,8,9]]
for i in range(0,len(list)):
    print(i,list[i])
#print(list)

#flatten_list = [val for sublist in list for val in sublist]
flatten_list = []
for sublist in list:
    for val in sublist:
        flatten_list.append(val)
print(flatten_list)