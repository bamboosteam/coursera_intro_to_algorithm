# This file contains all of the 100,000 integers between 1 and 100,000 (inclusive) in some order, with no integer repeated.
#
#  Your task is to compute the number of inversions in the file given, where the i^{th}i
# th
#   row of the file indicates the i^{th}i
# th
#   entry of an array.
#
#   Because of the large size of this array, you should implement the fast divide-and-conquer algorithm covered in the video lectures.
#
# The numeric answer for the given input file should be typed in the space below.
#
# So if your answer is 1198233847, then just type 1198233847 in the space provided without any space / commas / any other punctuation marks. You can make up to 5 attempts, and we'll use the best one for grading.
#
# (We do not require you to submit your code, so feel free to use any programming language you want --- just type the final numeric answer in the following space.)
#
# [TIP: before submitting, first test the correctness of your program on some small test files or your own devising.  Then post your best test cases to the discussion forums to help your fellow students!]
#
# answer for input.txt : 2407905288

def txt_to_array(path):
    test_file = open(path, "r")
    lines = test_file.read().splitlines()
    return lines

def brute_force_inversions(array):
    n = len(array)
    res = 0
    for i in range(n):
        for j in range(i, n):
            if int(array[i]) > int(array[j]):
                res += 1
    return res

def split_count(array):
    n = len(array)
    if n == 1:
        return 0
    else:
        half = int(n/2)
        left, right = array[0:half], array[half:n]
        print(left)
        x = split_count(left)
        y = split_count(right)
        return int(x) + int(y)

array = txt_to_array("input2.txt")
print(split_count(array))
