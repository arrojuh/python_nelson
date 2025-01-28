## LOOPS
## FOR AND WHILE LOOP

# FOR LOOP works within a specified range
# While LOOP works within the boundary of condition

k = range(0,100)
type(k)

# syntax for for loop

''' for item in iterable:
        do something''' #iterable could be anything with single/multiple values

for i in range(0,10):
    print(i)

for i in ['a','b','c','d']:
    print(i)

dict1 ={'a':1,'b':2,'c':3}

for key in dict1.keys():
    print(key)

for value in dict1.values():
    print(value)

for key,value in dict1.items():
    print(key,value)

for i in range(1,5):
    for j in range(i,9):
        print(i,";",j)


# WHILE LOOP

'''while conditon:
        do something''' # it works until the condition is true and stops when its false


num = 0
while num>10:
    print(num)
    num = num+1#equals to num +=1


cond = True
num = 0
while cond:
    print(num)
    if num == 20:
        cond = False
    num = num+1


    


print(dict1.keys(),dict1.values(),dict1.items())