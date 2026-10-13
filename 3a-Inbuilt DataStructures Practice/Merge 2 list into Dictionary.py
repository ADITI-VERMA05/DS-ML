def merge_lists_to_dictionary(keys, values):
    if len(keys) != len(values):
        return False
    return dict(zip(keys, values))
