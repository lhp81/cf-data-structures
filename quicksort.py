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
    less = quicksort(less)  # have to redefine these vars because otherwise
                            # everything gets screwed up below.
    greater = quicksort(greater)
    results += less
    results += equal
    results += greater
    return results


if __name__ == '__main__':
    test_random_list = []
    test_ordered_list = []

    for i in range(1000):
        test_random_list.append(random.randint(0, 10000))

    for i in range(1000):
        test_ordered_list.append(i)

    start_time = time.time()
    quicksort(test_random_list)
    mid_time = time.time()
    quicksort(test_ordered_list)
    end_time = time.time()

    print "Time to sort a random list of 1000 numbers in range(0,9999):"
    print mid_time - start_time, 'seconds'
    print "Time to sort a list of 1000 numbers from 0-9999:"
    print end_time - mid_time, 'seconds'
