from random import randint
from linked_list import List


def sort(array):
    if len(array) > 1:
        pivot = (min(array)+max(array))/2
        left = List()
        right = List()
        equals = List()
        for x in array:
            if x < pivot:
                left.push(x)
            elif x > pivot:
                right.push(x)
            elif x == pivot:
                equals.push(x)
        return sort(left) + equals + sort(right)
    else:
        return array

a = List()
for i in range(15):
    a.push(randint(0, 100))
print(a)
print(sort(a))
