
def radix(li):
    buckets = []  # to hold 0 through 9
    # ok, here's an uuuuugly way to find out how far to go.
    ugly_counter = [len(str(i)) for i in li]
    as_far_as_we_go = max(ugly_counter)
    # it ain't pretty but it works.
    for i in range(10):
        buckets.append([])
        # buckets[0] is for 0s, buckets[1] for 1s, &c.
    counter = 1
    work_list = [num for num in list]
    while counter <= as_far_as_we_go:
        for number in work_list:
            buckets[number % counter].append(number)
        empty_catcher = []
        for bucket in buckets:
            for number in bucket:
                empty_catcher.extend(number)
        work_list = empty_catcher
        counter += 1
    return sorted_list
