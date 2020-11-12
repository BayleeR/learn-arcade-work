import random


def selection_sort(my_list):
    """ Sort a list using the selection sort """

    selection_outside_count = 0
    selection_inside_count = 0
    for cur_pos in range(len(my_list)):
        min_pos = cur_pos
        selection_outside_count += 1  # count how many times outside loop loops
        for scan_pos in range(cur_pos + 1, len(my_list)):
            selection_inside_count += 1  # count how many times inside loop loops
            if my_list[scan_pos] < my_list[min_pos]:
                min_pos = scan_pos

        temp = my_list[min_pos]
        my_list[min_pos] = my_list[cur_pos]
        my_list[cur_pos] = temp
    print("Selection sort, outside loop ran", selection_outside_count, "times.")
    print("Selection sort, inside loop ran", selection_inside_count, "times.")


def insertion_sort(my_list):
    """ Sort a list using the insertion sort """

    insertion_outside_count = 0
    insertion_inside_count = 0
    for key_pos in range(1, len(my_list)):
        insertion_outside_count += 1
        key_value = my_list[key_pos]
        scan_pos = key_pos - 1
        while (scan_pos >= 0) and (my_list[scan_pos] > key_value):
            my_list[scan_pos + 1] = my_list[scan_pos]
            scan_pos = scan_pos - 1
            insertion_inside_count += 1
        my_list[scan_pos + 1] = key_value
    print("Insertion sort, outside loop ran", insertion_outside_count, "times.")
    print("Insertion sort, inside loop ran", insertion_inside_count, "times.")

# This will point out a list
# For more information on the print formatting {:3}
# see the chapter on print formatting.


def print_list(my_list):
    for item in my_list:
        print(f"{item:3}", end="")
    print()


def main():
    # Create two lists of the same random numbers
    list_for_selection_sort = []
    list_for_insertion_sort = []
    list_size = 100
    for i in range(list_size):
        new_number = random.randrange(100)
        list_for_selection_sort.append(new_number)
        list_for_insertion_sort.append(new_number)

    # Print the original list
    print("Original List")
    print_list(list_for_selection_sort)

    # Use the selection sort and print the result
    print("Selection Sort")
    selection_sort(list_for_selection_sort)
    print_list(list_for_selection_sort)

    # Use the insertion sort and print the result
    print("Insertion Sort")
    insertion_sort(list_for_insertion_sort)
    print_list(list_for_insertion_sort)


main()