arr = [10, 55, 45, 61, 59, 66]

for i in range(len(arr)-1):
    for j in range(len(arr)-1):
        if arr[j]>arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print("\n Ascending Order: ",arr)

lst = [10, 55, 45, 61, 59, 66]

for i in range(len(lst)-1):
    for j in range(len(lst)-1):
        if lst[j]<lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]

print("\n Descending Order: ",lst)
print("\n")