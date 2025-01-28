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

for key,value in dict1.items():
    print(key,value)


