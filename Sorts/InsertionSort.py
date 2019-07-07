# @author Kristen Lee
# @date July-07-2019

from random import randint

# Create an array of 100 with random ints between 0-199
random_array = []
for x in range(0,100):
    random_array.append(randint(0,200))
print "length of array is " + str(len(random_array))

# Insertion sort the random array
def insertion_sort(array_to_sort):
    i = 1
    while i < len(array_to_sort):
        x = array_to_sort[i]
        j = i - 1
        while j >= 0 and array_to_sort[j] > x:
            array_to_sort[j+1] = array_to_sort[j]
            j -= 1
        array_to_sort[j+1] = x
        i += 1
    return is_sorted(array_to_sort)

# Checks if an array of ints is properly sorted
def is_sorted(array):
    i = 0
    j = 1
    for x in array:
        if array[i] > array[j]:
            return False
    return True

print "array is sorted: " + str(insertion_sort(random_array))
