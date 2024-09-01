lst = [10, 20, 30, 40, 50, 60, 70, 80]
low = 0
high = len(lst)-1
mid = (low+high)//2
key = int(input("\n Enter Element to Search: "))
flag = False
loc = 0

while low<=high:
    mid = (low+high)//2
    
    if key == lst[mid]:
        flag = True
        loc = mid
        break

    elif key < lst[mid]:
        high = mid - 1
        
    else:
        low = mid + 1

if flag == True:
    print("\n Element found", loc)

else:
    print("\n Element not found in the list")