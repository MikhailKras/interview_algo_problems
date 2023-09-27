# Binsearch

def search(arr, value):
    if not arr:
        return False
    left, right = 0, len(arr) - 1
    while left < right:
        m = (left + right) // 2
        if arr[m] >= value:
            right = m
        else:
            left = m + 1
    return arr[left] == value


lst = [1, 2, 3, 4, 8, 10]
value = 4
print(search(lst, value))
