# 2.
# GENERAL DIRECTIONS AND HOW TO GIVE US YOUR ANSWER:
#
# See the first question.
#
# DIRECTIONS FOR THIS PROBLEM:
#
# Compute the number of comparisons (as in Problem 1), always using the final element of the given array as the pivot element.  Again, be sure to implement the Partition subroutine exactly as it is described in the video lectures.
#
# Recall from the lectures that, just before the main Partition subroutine, you should exchange the pivot element (i.e., the last element) with the first element.

# wrong answer = 160361
# correct answer = 164123


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
        p = array[-1]
        comparisons = 0
        # rearrange array so that the pivot is in the first place
        array[0], array[-1] = p, array[0]
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
        first_sorted, first_count = quick_sort_last_pivot(first, comparison)
        second_sorted, second_count = quick_sort_last_pivot(second, comparison)
        p_array = [p]
        comparison += first_count + second_count + n - 1
        return first_sorted + p_array + second_sorted, comparison
        # i = 0
        # for k in range(0, n-1):
        #     if int(p) > int(array[k]):
        #         tmp = array[k]
        #         array[k] = array[i]
        #         array[i] = tmp
        #         i += 1
        # array[-1], array[i] = array[i], p
        # first, second = array[0:i], array[i+1:n]
        # first_sorted, first_comparison = quick_sort_last_pivot(first, comparison)
        # second_sorted, second_comparison = quick_sort_last_pivot(second, comparison)
        # p_array = [p]
        # comparison += first_comparison + second_comparison + n - 1
        # return first_sorted + p_array + second_sorted, comparison

print(array)
print(quick_sort_last_pivot(array, comparison))
