import random
import time


def insertion_sort(li):
    for i in range(1, len(li)):  # start at li[1]; counter gets li[0]
        counter = i  # seems silly to have to define this here
        while (counter >= 0 and i > 0):
            counter -= 1
            if li[i] < li[counter]:
                li[i], li[counter] = li[counter], li[i]
            i -= 1  # so we can iterate backwards through the list
            counter = i  # this will get knocked down by 1 once we go to top
    return li


if __name__ == '__main__':
    best_case = []
    average_case = []
    worst_case = []
    for i in range(0, 100):
        best_case.append(i)
    for i in range(0, 100):
        average_case.append(random.randint(0, 10000))
    for i in range(100, 0, -1):
        worst_case.append(i)
    first_time = time.time()
    insertion_sort(best_case)
    second_time = time.time()
    insertion_sort(average_case)
    third_time = time.time()
    insertion_sort(worst_case)
    fourth_time = time.time()
    print "It took", second_time - first_time, "seconds for a lame best case "\
    "scenario."
    print "It took", third_time - second_time, "seconds for a so-so avg case."
    print "It took", fourth_time - third_time, "seconds for a lame worst case."
