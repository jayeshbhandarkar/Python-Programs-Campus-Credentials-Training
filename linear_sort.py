# Ascending Order - Linear Sorting

"""
arr = [10, 55, 45, 61, 59, 2, 66]
loc = 0
min = 0

for i in range(len(arr)-1):
    min=arr[i]
    loc=i

    for j in range(i+1, len(arr)):
        if min > arr[j]:
            min = arr[j]
            loc = j

    arr[i], arr[loc] = arr[loc], arr[i]

print(arr)
"""

# Descending Order - Linear Sorting

arr = [10, 55, 45, 61, 59, 2, 66]
loc = 0
max = 0

for i in range(len(arr)):
    max=arr[i]
    loc=i

    for j in range(i+1, len(arr)):
        if max < arr[j]:
            max = arr[j]
            loc = j

    arr[i], arr[loc] = arr[loc], arr[i]

print(arr)
