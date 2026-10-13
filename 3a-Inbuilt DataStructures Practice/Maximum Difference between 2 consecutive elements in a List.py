def max_consecutive_difference(lst):
    max_diff = 0
    for i in range(len(lst) - 1):
        diff = lst[i] - lst[i + 1]
        if diff < 0:
            diff = -diff  # taking absolute value manually
        if diff > max_diff:
            max_diff = diff
    return max_diff
