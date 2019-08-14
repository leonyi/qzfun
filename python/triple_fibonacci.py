#!/usr/bin/env python3
# Sum of elements of first three indexes in given array and then make the subsequent value.


def count_elements(ar):
    return sum(ar[:])


def triple_fibonacci(ar, countreps):

    if len(ar) < 3:
        print("Invalid array size: {}".format(len(ar)))
        return False
    for n in range(countreps):
        if n == 0:
            esum = count_elements(ar)
        else:
            esum = count_elements(ar[n:])
        print("array: {} and count: {}".format(ar, esum))
        ar.append(esum)

    return ar


def triple_fibonacci_rec(ar, countreps):

    for n in range(countreps):
        ar.append(sum(ar[n:]))

    return ar


###############
# Control Code
###############
ar = [1, 1, 1]
countreps = 7

#print(f'Result: {triple_fibonacci(ar,countreps)}')
#########
# OUTPUT:
# (python-world3) yleon@khalessi ~/Desktop/Algos/PhoneChallenges/phone_challenges »./triple_fibonacci.py
# array: [1, 1, 1] and count: 3
# array: [1, 1, 1, 3] and count: 5
# array: [1, 1, 1, 3, 5] and count: 9
# array: [1, 1, 1, 3, 5, 9] and count: 17
# array: [1, 1, 1, 3, 5, 9, 17] and count: 31
# array: [1, 1, 1, 3, 5, 9, 17, 31] and count: 57
# array: [1, 1, 1, 3, 5, 9, 17, 31, 57] and count: 105
# Result: [1, 1, 1, 3, 5, 9, 17, 31, 57, 105]

print(f'Result: {triple_fibonacci_rec(ar,countreps)}')
# OUTPUT:
# (python-world3) yleon@khalessi ~/Desktop/Algos/PhoneChallenges/phone_challenges »./triple_fibonacci.py
# Result: [1, 1, 1, 3, 5, 9, 17, 31, 57, 105]
