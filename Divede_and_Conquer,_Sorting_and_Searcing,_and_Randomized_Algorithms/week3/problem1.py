# 1.
#
# The file contains all of the integers between 1 and 10,000 (inclusive, with no repeats) in unsorted order.  The integer in the i^{th}i
# th
#   row of the file gives you the i^{th}i
# th
#   entry of an input array.
#
#  Your task is to compute the total number of comparisons used to sort the given input file by QuickSort.  As you know, the number of comparisons depends on which elements are chosen as pivots, so we'll ask you to explore three different pivoting rules.
#
# You should not count comparisons one-by-one.  Rather, when there is a recursive call on a subarray of length m, you should simply add m-1 to your running total of comparisons.  (This is because the pivot element is compared to each of the other m-1 elements in the subarray in this recursive call.)
#
# WARNING: The Partition subroutine can be implemented in several different ways, and different implementations can give you differing numbers of comparisons.  For this problem, you should implement the Partition subroutine exactly as it is described in the video lectures (otherwise you might get the wrong answer).
#
# DIRECTIONS FOR THIS PROBLEM:
#
# For the first part of the programming assignment, you should always use the first element of the array as the pivot element.
#
# HOW TO GIVE US YOUR ANSWER:
#
# Type the numeric answer in the space provided.
#
# So if your answer is 1198233847, then just type 1198233847 in the space provided without any space / commas / other punctuation marks. You have 5 attempts to get the correct answer.
#
# (We do not require you to submit your code, so feel free to use the programming language of your choice, just type the numeric answer in the following space.)

def txt_to_array(path):
    test_file = open(path, "r")
    lines = test_file.read().splitlines()
    return lines

array = txt_to_array("QuickSort.txt")
comparison = 0

def quick_sort_first_pivot(array, comparison):
    n = len(array)
    if n <= 1:
        return array, 0
    else:
        p = array[0]
        # partition array around the p (pivot)
        # i is set as boundary between the pivot and the rest.
        i = 1
        for k in range(1, n):
            if int(p) > int(array[k]):
                tmp = array[k]
                array[k] = array[i]
                array[i] = tmp
                i += 1
        array[0], array[i - 1] = array[i - 1], p
        first, second = array[0:i-1], array[i:n]
        first_sorted, first_count = quick_sort_first_pivot(first, comparison)
        second_sorted, second_count = quick_sort_first_pivot(second, comparison)
        p_array = [p]
        comparison += first_count + second_count + n - 1
        print(comparison)
        return first_sorted + p_array + second_sorted, comparison

print(quick_sort_first_pivot(array, comparison))
