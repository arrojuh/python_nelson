## Lets user do the same operation with different arguments and run multiple times.

'''
syntax 

def function_name(arguments(*args,**kwargs)):
    operations
    return

'''

list1= [1,2,3,4,6,7,8]
 x = 15
 sq = x**3
 print(sq)

for i in list1:
    for j in [3,4,5]:
        sq= i**j
        print(sq)

    
def power(val1,val2):
    for i in val1:
        for j in val2:
            sq= i**j
            print(sq)
    return sq


power(list1,[1,2,3])
val3 = power([4,5,6],[1,2,3])

print(val3)

dict1 = {'A':{'member':12345,'Balance':300},\
    'B':{'member':23456,'Balance':234},\
    'C':{'member':74789,'Balance':8887},\
    'D':{'member':33456,'Balance':3012}}
dict2 = {'A':{'member':12345,'Balance':300},\
    'B':{'member':23456,'Balance':234},\
    'C':{'member':74789,'Balance':8887},\
    'D':{'member':33456,'Balance':3012}}
dict3 = {'A':{'member':12345,'Balance':300},\
    'B':{'member':23456,'Balance':234},\
    'C':{'member':74789,'Balance':8887},\
    'D':{'member':33456,'Balance':3012}}
dict4 = {'A':{'member':12345,'Balance':300},\
    'B':{'member':23456,'Balance':234},\
    'C':{'member':74789,'Balance':8887},\
    'D':{'member':33456,'Balance':3012}}
dict5 = {'A':{'member':12345,'Balance':300},\
    'B':{'member':23456,'Balance':234},\
    'C':{'member':74789,'Balance':8887},\
    'D':{'member':33456,'Balance':3012}}


#1 -- Multiple Banks Data 
#2 -- Multiple Category Consumers -- Individual, Corporate, Joint
#3 -- limited options in transaction

options1 = ['Balance(B)', 'Withdraw(W)', 'Deposit(D)','Cardless Withdrawl(CW)',\
     'Cardless Deposit(CD)', 'Transfer(T)','PIN CHANGE(P)']

options2 = ['Balance(B)', 'Withdraw(W)', 'Deposit(D)']

options3 =['Balance(B)', 'Withdraw(W)', 'Deposit(D)', 'Transfer(T)','PIN CHANGE(P)']

options4 =  ['Balance(B)', 'Withdraw(W)', 'Deposit(D)','Cardless Withdrawl(CW)',\
     'Cardless Deposit(CD)']
 
def bank(data,cat,options):
    check = True
    while check:
        start_stop = input('Do you want to start the Transaction(Y for yes and N for No)::')
        if start_stop.lower() == 'y':
            print('You chose to Run')
            print('Welcome to the ATM')
            if (cat == 1)| (cat=='1'):
                actn = input('Enter your 5 digit account number::')
            if (cat == 2)| (cat=='2'):
                actn = input('Enter your 6 digit account number::')
            if (cat == 3)| (cat=='3'):
                actn = input('Enter your 7 digit account number::')
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
                for key in data.keys():
                    if data[key]['member']==actn:
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

            display = 'select the option from '

            for i in options:
                display = display + str(i)+ str(',')

            display = display[:-1]+ ' :: '
            option = input(display)

            if (option.lower() =='w') or (option.lower()=='d'):
                print('Your Balance is :: ',data[key1]['Balance'])
                amt = input('Enter the Amount::')
                check5= True
                while check5:
                    try:
                        amt = int(amt)
                        check5= False
                        
                    except:
                        amt = input('Enter the Integer Amount::')
            else:
                print('Your Balance is :: ',data[key1]['Balance'])
            
            if option.lower() == 'w':
                data[key1]['Balance'] = data[key1]['Balance']-amt
            if option.lower() == 'd':
                data[key1]['Balance'] = data[key1]['Balance']+amt

            print('Your Updated Balance is :: ',data[key1]['Balance'])
            print('Thanks for Banking with us')                    
        else:               
            print('You Choose to stop')
            check = False
            # do not run


