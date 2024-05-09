def split_array_into_groups(arr, group_size):
    return [arr[i:i + group_size] for i in range(0, len(arr), group_size)]
