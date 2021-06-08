
# In this programming assignment you will implement one or more of the integer multiplication algorithms described in lecture.
#
# To get the most out of this assignment, your program should restrict itself to multiplying only pairs of single-digit numbers.  You can implement the grade-school algorithm if you want, but to get the most out of the assignment you'll want to implement recursive integer multiplication and/or Karatsuba's algorithm.
#
# So: what's the product of the following two 64-digit numbers?
#
# 3141592653589793238462643383279502884197169399375105820974944592
#
# 2718281828459045235360287471352662497757247093699959574966967627
#
# [TIP: before submitting, first test the correctness of your program on some small test cases of your own devising. Then post your best test cases to the discussion forums to help your fellow students!]
#
# [Food for thought: the number of digits in each input number is a power of 2.  Does this make your life easier?  Does it depend on which algorithm you're implementing?]
#
# The numeric answer should be typed in the space below.  So if your answer is 1198233847, then just type 1198233847 in the space provided without any space / commas / any other punctuation marks.
#
# (We do not require you to submit your code, so feel free to use any programming language you want --- just type the final numeric answer in the following space.)


# Following code tries to implement Karatsuba multiplication


x = 3141592653589793238462643383279502884197169399375105820974944592
y = 2718281828459045235360287471352662497757247093699959574966967627

def integer(x):
    if x == '':
        return 0
    else:
        return int(x)


def Karatsuba(x, y):
    n = len(str(x))
    if n == 1:
        return integer(x)*integer(y)

    else:
        half = int(n/2)
        a, b = str(x)[0:half], str(x)[half:n]
        c, d = str(y)[0:half], str(y)[half:n]
        print('a=' + a, 'b=' + b, 'c='+c, 'd='+d, x, y)
        p, q = integer(a) + integer(b), integer(c) + integer(d)
        # when calculating p, q, their digits are not set as a power of 2 in some cases, that's why it does'nt work for all cases.
        ac = Karatsuba(a, c)
        # print(ac)
        bd = Karatsuba(b, d)
        ad = Karatsuba(a, d)
        bc = Karatsuba(b, c)
        # pq = Karatsuba(p, q)
        # adbc = pq - ac - bd
    return (10**n)*ac + (10**half)*(ad+bc) + bd

print(Karatsuba(x, y))
