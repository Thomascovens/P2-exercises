# Write your code here

def median(ns):
    sort = sorted(ns)
    i = len(sort) // 2
    if len(sort) % 2 == 0:
        return (sort[i - 1] + sort[i]) / 2
    else:
        return sort[i]


median([50, 20, 100, 40, 20])
