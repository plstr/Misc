# the_list = [84, 69, 76, 86, 94, 91, 2, 44, 31, 9, 74, 11, 16]
the_list = [7, 4, 2, 3, 6, 9, 5, 8, 0, 1]

for i in range(len(the_list)):
    for j in range(len(the_list)):
        if the_list[i] < the_list[j]:
            temp = the_list[i]
            the_list[i] = the_list[j]
            the_list[j] = temp
    print the_list
print "finally: ", the_list
