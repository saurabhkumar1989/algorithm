def binary_search(a, query):
    minimum = 0
    maximum = len(a) - 1
    while True:
        index = (minimum + maximum) // 2
        if maximum < minimum:
            return -1
        if a[index] < query:
            minimum = index + 1
        elif a[index] > query:
            maximum = index - 1
        else:
            return index
if __name__ == "__main__":
    a = [11,21,31,41,51,61,71,81,91]
    query = 9
    print binary_search(a,query)
