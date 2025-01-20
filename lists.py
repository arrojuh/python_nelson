list1 = ['a',1,'$%@',3.0]
#two ways to create lists
met1 = ['a','hari',1,5.8]
met2 = list('Harikrishna')#iterable ---> which has individual elements collected together
print(met1,met2)
list3 = list((1,2,3,'A'))
print(tuple('Harikrishna'))
print(set("Harikrishna"))
print(list3)
# (iter) --> tuple
# [iter]--> List
# {iter} --> Set
# {'key':'value} --> Dictionary
print(list({1,2,3,4}))


######-----------------------##########
##list()--- converts the iterable to list
##[] ----- puts the elements into the list

#example
tup1 = ('A','B','C')
list1 = list(tup1) ## convert the tuple to list --convert the datatype
list2 = [tup1]## inserts the tuple into the list -- adding the element to the list

print(list1,list2)

print(list1[0],list2[0])

## Accessing The List

list1[1] # index

list1[0:2] # slicing

list1[0:3:2] # step slicing

list1[-1]

list1[::-1] # 

list1

#nested index

list1.extend(list2)

print(list1)

val1= list1[-1]
val2 = val1[1]
print(val2)

list4 = [1,2,3,4]

list5 = [5,6,7,8]

list1.append(list4) # adds the list4 to the list1 as an element

print(list1)

list1.extend(list5)  # absorbs all the elements from list5 to list1

print(list1)

print(list1[-5][-2])

#append --> add an element to the list

list1.append('E') # .method doesn't require to be updated in a variable

#adding two lists
list3 = list1 + list2 # every other method needs to be used saved in a varible

list3

list1.extend(list2)

list1

# insert at a specific index

list1.insert(1,'T')#---> .insert(index,value)

list1

#removing a value from the list

list1.pop() # removes last element from the list
print(list1)

x = list1.index('D')
print(x)

list1.remove(list1[x]) #removes the specified value from the list

list1

# get the index of the element

list1.index('C') # gives the index of the element


# to remove a value from string

str1 = 'Washington'

str1[0:3]+str1[4:]

# clearing the list
list1.clear()
print(list1)

list5

# updating an element in the list
list5[2] = 10
list5

# count

list5.append(5)

# number of occurences of an element
list5.count(5)

# sorting the llist

list5.sort()
list5

# copying the list

list5
list6 = list5 # this method will make sure any change in any list affects both
print(list5,list6)

list6[2]= 200

print(list5,list6)

list7 = list5.copy() # creates a shallow copy, doesnt affect when there is a modification
print(list5,list7)

list7[-1] = 'ABC'
print(list5,list7)

# replication of a list
list7*3











