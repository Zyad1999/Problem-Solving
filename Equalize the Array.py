def equalizeArray(arr):
    e = max(set(arr), key = arr.count)
    return len(arr)-arr.count(e)