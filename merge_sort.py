# original implementation of a merge sort.
import random
import time


def merge_sort(list):
    if len(list) < 2:
        return list
    l_length = len(list)
    l_div = l_length // 2
    one = merge_sort(list[:l_div])
    two = merge_sort(list[l_div:])
    results = []
    one_count = 0
    two_count = 0
    while (len(one) > one_count) and (len(two) > two_count):
        if one[one_count] < two[two_count]:
            results.append(one[one_count])
            one_count += 1
        else:
            results.append(two[two_count])
            two_count += 1
    results.extend(two[two_count:])
    results.extend(one[one_count:])
    return results

if __name__ == '__main__':
    test = []
    for i in range(1000):
        test.append(random.randint(0, 10000))
    sorted = []
    for i in range(1000):
        sorted.append(i)
    first_time = time.time()
    merge_sort(test)
    second_time = time.time()
    merge_sort(sorted)
    last_time = time.time()
    print 'My merge sort took', second_time - first_time, 'seconds to sort'\
        ' 1000 numbers in random order.' \
    '\nIt then took', last_time - second_time, 'seconds to sort 0-999.'
