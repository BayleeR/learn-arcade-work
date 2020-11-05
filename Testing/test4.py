"""my_list = [15, 57, 14, 33, 72, 79, 26, 56, 42, 40]

print(my_list)

temp = my_list[0] #store position 0 (number 15)
my_list[0] = my_list[2]
my_list[2] = temp

#or you can do it this way

my_list[0], my_list[2] = my_list[2], my_list[0]

print(my_list)"""

"""15, 57, 14, 33, 72, 79, 26, 56, 42, 40
#scan from left to right
#looks for the smallest number, which is 14, so 14 switches places with the first number, which is 14
#now we have at least 1 number sorted
14, 57, 15, 33, 72, 79, 26, 56, 42, 40
#looks for the next smallest number (not including 14), and finds 15, so it switches 15 and 57
14, 15, 57, 33, 72, 79, 26, 56, 42, 40
14, 15, 26, 33, 72, 79, 57, 56, 42, 40
14, 15, 26, 33, 72, 79, 57, 56, 42, 40
14, 15, 26, 33, 40, 79, 57, 56, 42, 72
14, 15, 26, 33, 40, 42, 57, 56, 79, 72
14, 15, 26, 33, 40, 42, 56, 57, 79, 72
14, 15, 26, 33, 40, 42, 56, 57, 72, 79"""


def selection_sort(my_list):

    for cur_pos in range(len(my_list)): # going to loop 10 times (because you have 10 numbers)
        min_pos = cur_pos
        for scan_pos in range(cur_pos + 1, len(my_list)): # you don't want to scan 14 to see if it's smaller than 14, so you add 1
            if my_list[scan_pos] < my_list[min_pos]:
                min_pos = scan_pos
                #loop above loops from 1-9, then 2-9, etc

            # this code swaps the two values
            temp = my_list[min_pos]
            my_list[min_pos] = my_list[cur_pos]
            my_list[cur_pos] = temp


my_list = [15, 57, 14, 33, 72, 79, 26, 56, 42, 40]
selection_sort(my_list)
print(my_list)


