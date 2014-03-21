
def radix(li):
    buckets = []  # to hold 0 through 9
    for i in range(10):
        buckets.append([])
        # buckets[0] is for 0s, buckets[1] for 1s, &c.
    