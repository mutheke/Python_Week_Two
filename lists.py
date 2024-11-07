# empty list 
my_list = []
#Append the following elements to my_list: 10, 20, 30, 40.
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)
#Insert the value 15 at the second position in the list.
my_list[2] = 15
print(my_list)
my_list2 = [50, 60, 70]
#Extend my_list with another list: [50, 60, 70].
my_list.extend(my_list2)
print(my_list)
#Remove the last element from my_list.
my_list.remove(my_list[-1])
print(my_list)
#Sort my_list in ascending order.

my_list.sort()
print(my_list)
#Find and print the index of the value 30 in my_list
my_list = [10, 20, 30, 40,50, 60, 70]
index_of = my_list.index(30)
print(index_of)
