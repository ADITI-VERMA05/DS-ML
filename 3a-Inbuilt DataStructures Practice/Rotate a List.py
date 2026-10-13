def rotate_list(lst, k):
    n = len(lst)
    if n == 0:
        return lst  # return empty list as is

    k = k % n  # handle k > n
    rotated = []

    # Step 1: Add last k elements to the new list
    for i in range(n - k, n):
        rotated.append(lst[i])

    # Step 2: Add the remaining elements from the start
    for i in range(n - k):
        rotated.append(lst[i])

    return rotated
