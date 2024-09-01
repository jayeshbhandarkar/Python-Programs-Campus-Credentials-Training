# lambda function is a anonymous function

"""l1 = [2,-3,5,-6,7,-8,-9]
l2 = list(map(lambda x: -x, l1))

l3 = list(map(lambda x: x**3, l1))

print(l2,l3)"""

"""def square(n):
    return n*n

s = lambda n: n*n

print("The Square of 4 is",square(4))
print("The Square of 5 is",s(5))"""


"""def sum(a,b):
    return a+b

add = lambda a,b: a+b

print("The Sum of 4 is",sum(4,5))
print("The Sum of 5 is",add(5,6))"""


def large(a,b):
    if a>b:
        return a
    
    else:
        return b
    
l = lambda a,b : a if a>b else b

print("The largest number is",large(4,5))
print("The largest number is",l(5,8))