# original implementation of a merge sort.

def merge_sort(l):
    if len(l) < 2:
        return l
    l_length = len(l)
    l_div = l_length / 2
    set_one = l[0:l_div]
    set_two = l[l_div:]
