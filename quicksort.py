import random
import time


def quicksort(li):
    if len(li) < 2:
        return li
    pivot = li[random.randint(0, (len(li)-1))]
    # choose a random number to be the pivot since this is a good practice,
    # according to wikipedia.
    less = [x for x in li if x < pivot]
    greater = [x for x in li if x > pivot]
    equal = [x for x in li if x == pivot]
    results = []
    less = quicksort(less)  # got this out from rosettacode. was getting
                            # errors before when I didn't have the assignment.
    greater = quicksort(greater)
    results += less
    results += equal
    results += greater
    return results

# if __name__ == '__main__':
    pass
