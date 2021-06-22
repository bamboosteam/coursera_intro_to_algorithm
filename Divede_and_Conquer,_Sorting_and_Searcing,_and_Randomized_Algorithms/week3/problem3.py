# 3.
# GENERAL DIRECTIONS AND HOW TO GIVE US YOUR ANSWER:
#
# See the first question.
#
# DIRECTIONS FOR THIS PROBLEM:
#
# Compute the number of comparisons (as in Problem 1), using the "median-of-three" pivot rule.  [The primary motivation behind this rule is to do a little bit of extra work to get much better performance on input arrays that are nearly sorted or reverse sorted.]  In more detail, you should choose the pivot as follows.
# Consider the first, middle, and final elements of the given array.
# (If the array has odd length it should be clear what the "middle" element is; for an array with even length 2k, use the kth element as the "middle" element. So for the array 4 5 6 7,  the "middle" element is the second one ---- 5 and not 6!)
# Identify which of these three elements is the median (i.e., the one whose value is in between the other two), and use this as your pivot.
# As discussed in the first and second parts of this programming assignment, be sure to implement Partition exactly as described in the video lectures (including exchanging the pivot element with the first element just before the main Partition subroutine).
#
# EXAMPLE: For the input array 8 2 4 5 7 1 you would consider the first (8), middle (4), and last (1) elements; since 4 is the median of the set {1,4,8}, you would use 4 as your pivot element.
#
# SUBTLE POINT: A careful analysis would keep track of the comparisons made in identifying the median of the three candidate elements.  You should NOT do this.  That is, as in the previous two problems, you should simply add m-1 to your running total of comparisons every time you recurse on a subarray with length m.
import statistics

def find_median(a, b, c):
    pass

def txt_to_array(path):
    test_file = open(path, "r")
    lines = test_file.read().splitlines()
    return lines

array = txt_to_array("QuickSort.txt")
comparison = 0

def quick_sort_last_pivot(array, comparison):
    n = len(array)
    if n <= 1:
        return array, 0
    else:
        if n % 2 == 0:
            p_array = [int(array[0]), int(array[int(n/2) - 1]), int(array[-1])]
        else:
            p_array = [int(array[0]), int(array[int((n-1)/2)]), int(array[-1])]
        p = str(statistics.median(p_array))
        position = array.index(p)
        # partition array around the p (pivot)
        # i is set as boundary between the pivot and the rest.
        if position != 0:
            array[0], array[position] = p, array[0]
        i = 1
        for k in range(1, n):
            if int(p) > int(array[k]):
                tmp = array[k]
                array[k] = array[i]
                array[i] = tmp
                i += 1
        array[0], array[i - 1] = array[i - 1], p
        first, second = array[0:i-1], array[i:n]
        first_sorted, first_comparison = quick_sort_last_pivot(first, comparison)
        second_sorted, second_comparison = quick_sort_last_pivot(second, comparison)
        p_array = [p]
        return first_sorted + p_array + second_sorted, comparison

print(array)
print(quick_sort_last_pivot(array, comparison))
