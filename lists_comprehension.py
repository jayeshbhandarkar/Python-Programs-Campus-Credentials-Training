'''
l1 = [2,3,4,5]
l2 = [4,6,8,10]

for i in l1:
    l2.append(i**2)

print(l2)
'''

"""
l = [1,2,3,4,5,6,7,8]
l1 = []

for i in l:
    if i!=5:
        l1.append(i)

print(l1)
"""


l1 = [2,5,3,4,7,6]
l2 = []

for i in l1:
    if i%2 == 0:
        l2.append(i)

    else:
        l2.append(i**2)
       
print(l2)
    