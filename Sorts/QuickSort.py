# @author Kristen Lee
# @date July-07-2019

from random import randint

# Create an array of 100 with random ints between 0-199
random_array = []
for x in range(0,100):
    random_array.append(randint(0,200))
print "length of array is " + str(len(random_array))

# quick sort the random array
def quick_sort(array_to_sort, lo, hi):
    if lo < hi:
        p = partition(array_to_sort, lo, hi)
        quick_sort(array_to_sort, lo, p)
        quick_sort(array_to_sort, p+1, hi)
    #mid_index = len(array_to_sort)/2
    #if array_to_sort[0] > array_to_sort[mid_index]:
    #    swap(0, mid_index, array_to_sort)
    #if array_to_sort[len(array_to_sort)-1] < array_to_sort[mid_index]:
    #    swap(len(array_to_sort)-1, mid_index, array_to_sort)
    #if array_to_sort[len(array_to_sort)-1] < array_to_sort[0]:
    #    swap(len(array_to_sort)-1, 0, array_to_sort)

def partition(array_to_sort, lo, hi):
    i = int(lo) + (int(hi) - int(lo)) / 2
    piv = array_to_sort[i]
    while True:
        while array_to_sort[lo] < piv:
            lo += 1
        while array_to_sort[hi] > piv:
            hi -= 1
        if lo >= hi:
            return hi
        swap(lo, hi, array_to_sort)
        lo += 1
        hi -= 1

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

quick_sort(random_array, 0, len(random_array)-1)
print "array is sorted: " + str(is_sorted(random_array))
