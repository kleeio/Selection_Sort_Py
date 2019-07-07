# @author Kristen Lee
# @date July-07-2019
from random import randint

# Create an array of 100 with random ints between 0-199.
random_array = []
for x in range(0,100):
    random_array.append(randint(0,200))
print "length of array is " + str(len(random_array))

# Selection sort the random array.
def selection_sort(array_to_sort):
    i = 0
    j = i + 1
    index = 0
    for x in array_to_sort:
        index = i
        for y in array_to_sort:
            if array_to_sort[j] < array_to_sort[index]:
                index = j
        if index != i:
            temp = array_to_sort[i]
            array_to_sort[i] = array_to_sort[index]
            array_to_sort[index] = temp
    return is_sorted(array_to_sort)

# Checks if an array of ints is properly sorted
def is_sorted(array):
    i = 0
    j = 1
    for x in array:
        if array[i] > array[j]:
            return False
    return True


print "the array is sorted: " + str(selection_sort(random_array))
