# if condition:  ### SINGULAR STATEMENT
    #do something

# if condition:  ## IF ELSE BLOCK
    # do something 
#else:
    # do something else

''' if condtion:
        do something
    elif condition:
        do something next
    else:
        do something else'''


a = 40

if a>10:
    print('greater')
elif a>100:
    print('much greater')
else:
    print('equal')

if a>10:
    print('greater ')
if a>100:
    print('much greater')
else:
    print('equal')


#### NESTED IF STATEMENT####

a = 100
b= 200

if a<200:
    c = a+b
    if b<300:
        if c>500:
            print('500')
        else:
            print('Not 500')
    else:
        print(b-a)
else:
    print('Nothing')


'''TAKING INPUT FROM USER'''

inpt = input('Please enter your name::') # takes the user input in string format

inpt_names = input('Please enter names with comma seperator:: ')

print(inpt_names)
print(inpt_names.split(','))# converting into a list using ','

# string to list
name1 = list('Harikrishna') # seperates each element and puts into the list
name2 = ['Harikrishna']
name3 = 'Harikrishna'.split('i') # creates a list by dividing the string at the seperator
print(name1,name2,name3)

mum = int('10')
print(mum)

number1 = int(input('Please enter the age:: ')) # converts the input to integer
number2 = float(input('Please enter the height:: ')) 

#check if a number is even or odd
num = int(input('Enter a number:: '))
if (num >0) and (num%2 == 0):
    print('Number is Even')
elif (num>0) and (num%2==1):
    print('Number is Odd')
else:
    print('Number is Negative')
