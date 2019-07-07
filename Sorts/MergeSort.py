# @author Kristen Lee
# @date July-07-2019
from random import randint

# Create an array of 100 with random ints between 0-199.
random_array = []
for x in range(0,100):
    random_array.append(randint(0,200))
print "length of array is " + str(len(random_array))

# Top-down implementation of merge sort for the given array
def merge_sort(array, spare_array, n):
    copy_array(array, 0, n, spare_array)
    split(spare_array, 0, n, array)
    return is_sorted(random_array)

# Splits given arrays down to elements of 2 or less
def split(spare_array, begin, end, array):
    if end - begin > 2:
        return
    middle = (end + begin) / 2
    split(array, begin, middle, spare_array)
    split(array, middle, end, spare_array)
    merge(spare_array, begin, middle, end, array)

# Merge the two given array
def merge(array, begin, middle, end, spare_array):
    i = begin
    j = middle
    k = begin
    for x in range[begin, end]:
        if i < middle and (j >= end or array[i] <= array[j]):
            spare_array[k] = array[i]
            i += 1
        else:
            spare_array[k] = array[j]
            j += 1
        k += 1

def copy_array(array, begin, end, spare_array):
    k = begin
    for x in range[begin, end]:
        spare_array[k] = array[k]
        k += 1
# swap the two given indexes from the array given
def swap(index_a, index_b, array):
    temp = array[index_a]
    array[index_a] = array[index_b]
    array[index_b] = temp

# Checks if an array of ints is properly sorted
def is_sorted(array):
    i = 0
    j = 1
    for x in array:
        if array[i] > array[j]:
            return False
    return True
spare = [None] * 100
print merge_sort(random_array, spare, 100)
