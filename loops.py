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

for i in range(1,10):
    for j in range(1,10-i):
        print('*',end = '')
    print('')


6
2,3,4,5


for i in range(2,100):
    check = True # this is a prime number
    for j in range(2,i):
        if i%j==0:
            check = False # this is not a prime number
            break
    if check == True: # its a prime number
        print(i)


for row in range(1, 10):
    for space in range(9, row, -1):
        print(" ",end=" ")
    for num in range(1, row):
        print(num, end=" ")
    for num2 in range(row, 0, -1):
        print(num2, end=" ")
    print()

for row in range(1, 9):
    for space in range(0, row):
        print(" ",end=" ")
    for num in range(1, 10-row):
        print(num, end=" ")
    print()




for i in range(1,20):
    print(i)
    for j in range(21,30):
        print(j,end=' ')
        if j == 25:
            break
    if i == 5:
        break
    print('')


dict1 = {'Hari':{'account_num':12345,'Balance':500},\
    'Krishna':{'account_num':23456,'Balance':1000},\
        'Vishal':{'account_num':45678,'Balance':2000}}

acn = int(input('Provide the Account Number::'))
with_dep = input('If you choose to Deposit enter "D" else for Withdraw enter "W"::')
amt = int(input('Enter the amount::'))

dict1.items()
dict1.keys()
dict1.values()

n = 5
p = 3
exp = 1
for i in range(0,p+1):
    exp = exp*n 

print(exp)


1st = 5 5*1 0
2nd = 25 5*5 1
3rd = 125 5*25 2

n*n
1st=  25 5*5 0
2nd= 125 25*5 1
3rd = 625



dict1 = {'A':{'member':12345,'Balance':300},\
    'B':{'member':23456,'Balance':234},\
    'C':{'member':74789,'Balance':8887},\
    'D':{'member':33456,'Balance':3012}}

#1 Start/Stop
#2 print Welcome
#3 Take the account number(5 digits only )
#3.1 Say Hi to the member
#4 Options- check the balance/withdraw/deposit
#5 Amt needs to be only numbers
        

        



        

check = True
while check:
    start_stop = input('Do you want to start the Transaction(Y for yes and N for No)::')
    if start_stop.lower() == 'y':
        print('You chose to Run')
        print('Welcome to the ATM')
        actn = input('Enter your 5 digit account number::')
        check1 = True
        while check1:
            if len(actn)!=5:
                actn = input('Please enter valid 5 digit account number::')
            else:
                try:
                    actn = int(actn)
                    check1= False
                except:  
                    actn = input('Please enter valid 5 digit account number in integers::')
        print('Account Number Entered:: ',actn)
        check3 = True
        key1 = ''
        while check3:
            for key in dict1.keys():
                if dict1[key]['member']==actn:
                    print('Hi,',key,' Welcome to the Bank')
                    key1 = key
                    check3 = False
                    break
            else:
                actn = input('Enter a valid account number associated with the bank::')
                check4= True
                while check4:
                    if len(actn)!=5:
                        actn = input('Please enter valid 5 digit account number::')
                    else:
                        try:
                            actn = int(actn)
                            check4= False
                        except:  
                            actn = input('Please enter valid 5 digit account number in integers::')

        option = input('select the option to Check the Balance(C), Withdraw(W),Deposit(D)::')

        if (option.lower() =='w') or (option.lower()=='d'):
            print('Your Balance is :: ',dict1[key1]['Balance'])
            amt = input('Enter the Amount::')
            check5= True
            while check5:
                try:
                    amt = int(amt)
                    check5= False
                    
                except:
                    amt = input('Enter the Integer Amount::')
        else:
            print('Your Balance is :: ',dict1[key1]['Balance'])
        
        if option.lower() == 'w':
            dict1[key1]['Balance'] = dict1[key1]['Balance']-amt
        if option.lower() == 'd':
            dict1[key1]['Balance'] = dict1[key1]['Balance']+amt

        print('Your Updated Balance is :: ',dict1[key1]['Balance'])
        print('Thanks for Banking with us')                    
    else:               
        print('You Choose to stop')
        check = False
        # do not run



















