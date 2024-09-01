# lists are ordered collection of elements which allows duplicates 
# lists are mutable

lst = [4,11,'Hello']

print(len(lst))

lst.append('Welcome')
print(lst)

lst.pop()
print(lst)

lst.remove('Hello')
print(lst)

lst.insert(2,'Python')
print(lst)

l1=['Welcome','to','Python','Programming']
l1.sort()
print(l1)

l1.sort(reverse=True)
print(l1)

if 'to' in l1:
    print("Yes")