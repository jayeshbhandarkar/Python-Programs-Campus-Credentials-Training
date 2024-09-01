lst = [10, 20, 55, 98, 56]
loc = 0
key = int(input("Enter Element to Search in the list: "))
flag = False

for x in range(len(lst)):
    if key == lst[x]:
        flag = True
        loc = x
        break

if flag:
    print("\n Element found at index", loc)

else:
    print("\n Element not found in the list")