def merge_dicts_with_overlapping_keys(dicts):
    merged = {}
    for d in dicts:
        for key, value in d.items():
            merged[key] = merged.get(key, 0) + value
    return merged