def insertion_sort(li):
    for i in range(1, len(li)):  # start at li[1]; ignore li[0]
        counter = i
        while counter >= 0:
            if li[i] > li[counter]:
                li[i], li[counter] = li[counter], li[i]
                j -= 1
    return li


if __name__ == '__main__':
    pass