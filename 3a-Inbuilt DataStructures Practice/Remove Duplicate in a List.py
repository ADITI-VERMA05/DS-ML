def remove_duplicates(lst):
    # Your code goes here
    unique_list = []
    for num in lst:
        is_duplicate = False
        for unique in unique_list:
            if num == unique:
                is_duplicate = True
                break
        if not is_duplicate:
            unique_list.append(num)
    return unique_list