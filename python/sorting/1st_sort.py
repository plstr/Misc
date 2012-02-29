def smallest_number(list):
    smallest = 9999999
    for i in list:
        if i < smallest:
            smallest = i
    return smallest

list = [23,44,1,2,33,4,1,2,3,455,8,9,56]
sorted_list = []

while len(list) > 0:
    temp = smallest_number(list)
    sorted_list.append(temp)
    list.remove(temp)

print sorted_list

