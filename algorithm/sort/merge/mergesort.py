def merge(l, r):
    result = []
    i = 0
    j = 0
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            result.append(l[i])
            i += 1
        else:
            result.append(r[j])
            j += 1

    result += l[i:]
    result += r[j:]
    return result


def merge_sort(l):
    if len(l) < 2:
        return l

    mid = len(l) // 2
    left = merge_sort(l[:mid])
    right = merge_sort(l[mid:])
    return merge(left, right)


l = [23, 41234, 12, 3451, 23, 512, 35, 1, 2, 5341, 45, 1, 3245, 13, 4, 1, 346, 1, 34, 6, 13, 46, 1, 346, 1, 36]
sorted_list = merge_sort(l)
assert sorted_list == sorted(l)