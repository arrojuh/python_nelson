# collection of key value pairs under {} is called as dictionary

# only strings,integers and tuples can be keys
dict1 = {'name':'harikrishna','names':['Hari','Krishna'],1:4.567,('a','b'):{1,2,3}}

dict2 = dict(name = 'Nelson',age = 30, address = 'U.S')  # rules for variable is applicable

print(dict1,dict2)

dict3 = dict([('phone',87020),('company','Deloitte')])
print(dict3)

# dict[key] will give the value corresponding to that key

print(dict1['name'],dict1[1])

print(dict1.keys(),dict1.values())

dict1['name'] # this gives error if key is not present
dict1.get('name')# this doesn't give an error when key is not present

dict1['kancn']
dict1.get('KeyboardInterruptneknwn   ng')

dict1['name'] = 'Arroju'
dict1

dict1.pop('name') # this remvoes the specified key value pair

dict1.popitem() # removes the last key value pair

dict1.update({'a':123}) # takes a dictionary as input

dict1.update(dict([('b',345)]))

'names' in dict1.keys()

dict3 = {'a':{'b':['1','2','3'],'c':{(6,7):[{100:'century'}]}}}
####     key  value
dict3['a']['c'][(6,7)][0][100]