def merge_three_dictionaries(dict1, dict2, dict3):
    merged_dict = {}
    merged_dict.update(dict1)
    merged_dict.update(dict2)
    merged_dict.update(dict3)
    return merged_dict
