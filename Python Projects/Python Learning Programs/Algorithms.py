# Algorithms

# Binary search

def binary_search(data, target):
    first = 0
    last = len(data) - 1
    while first <= last:
        mid = (first + last) // 2
        if data[mid] == target:
            return mid
        if data[mid] < target:
            first = mid + 1
        else:
            last = mid - 1

    return -1

print(binary_search([1, 2, 3, 4, 5, 6,], 4))  # Output: 3
print(binary_search([10, 20, 30, 40, 50], 25))  # Output: -1

#recursive binary search

def recursive_binary_search(data, target):
    return _search(data, target, 0, len(data) - 1)

def _search(data, target, first, last):
    if first > last:
        return -1
    mid = (first + last) // 2
    if data[mid] == target:
        return mid
    if data[mid] < target:
       return _search(data, target, mid + 1, last)
    else:
       return _search(data, target, first, mid - 1)
    

print(recursive_binary_search([1, 2, 3, 4, 5, 6,], 4))  # Output: 3
print(recursive_binary_search([1, 2, 3, 4, 5, 6,], 7))  # Output: -1