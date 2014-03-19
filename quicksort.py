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

if __name__ == '__main__':
    test_list = []
    time_catcher = []

    for i in range(1000):
        test_list.append(random.randint(0, 10000))

    for i in range(500):
        start_time = time.time()
        quicksort(test_list)
        end_time = time.time()
        time_catcher.append(end_time - start_time)

    print "Over 500 iterations of a list of 1,000 random numbers from "\
    "0-9,999, the longest sort time was", max(time_catcher), "sec, while the "\
    "shortest time was", min(time_catcher), "sec.\n"\
    "This gives a small demonstration of the efficacy of using a random value"\
    " as the pivot."
