def is_subset(lst1, lst2):
    for elem1 in lst1:
        found = False
        for elem2 in lst2:
            if elem1 == elem2:
                found = True
                break
        if not found:
            return False
    return True