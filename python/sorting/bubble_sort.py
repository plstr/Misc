# the_list = [84, 69, 76, 86, 94, 91, 2, 44, 31, 9, 74, 11, 16]
the_list = [7, 4, 2, 3, 6, 9, 5, 8, 0, 1]

counter = True
while counter: # to stop if all sorted
    counter = False
    for i in range(len(the_list)-1):
        print the_list
        if the_list[i] > the_list[i + 1]:
            temp = the_list[i]
            the_list[i] = the_list[i + 1]
            the_list[i + 1] = temp
            counter = True
print "finally: ", the_list
