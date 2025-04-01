### --- function inheritance-------------
def func_s(text):
    return text.upper()

def funcs2(func_s,text):
    new_text = func_s(text) # can use the capabilities of the function in this operation
    print(new_text)

# **kwargs
def func2(**kwards):
    for i,j in kwards.items():
        print(i,j)

func2(a=1,b=2,c=3)

## *args
def func1(*args):
    for i in args:
        print(i)

func1(1,2,3,4,5,6)


##Lambda function

art = lambda x: x**2

art(5)

art2 = lambda x,y: x**y

art2(5,4)


## problem statement

# replicate the game tic tac toe using python

'''
o|x|o
x|o|o
o|x|x
'''
#player1 = 'o'
#player2 = 'x'

## -- Ask the each user for input for their position and mark the position and print the table,
# use the keypad notation to mark the numbers

'''
1|2|3
4|5|6
7|8|9
'''

# take the user input for toss and toss the coin
# player1  --- heads
# toss -> heads
# player 1 chooses the marker and also plays first
# players will input the position number and the program should replace the position with the marker

# for example
# player 1 -> x -> 8
# player 2 -> o ->1

'''
o| |
 | |
 |x| 
'''
'''
use the following notation to mark your position
1|2|3
4|5|6
7|8|9
'''

### Hints table
'''
1) Create two markers and toss variables
2) use random module to pick the toss
3) assign the marker to the player who won and assign the other marker to the player who lost by default
4) create the table using spaces and '|'
5) keep the game running using while
6) when the positions(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7) has the same market the player wins
7) after every run we need to check for winning
8) make sure the input is within the ranges('x' and 'o' for markers and 1-9 for positions)
'''

dict1 = {'1':' ','2':' ','3':' ','t':'|'}

print(dict1['1'],dict1['t'],dict1['2'],dict1['t'],dict1['3'])

player_1 = int(input('enter 1,2,3')) ## x

dict1[str(player_1)]= 'x'
print(dict1['1'],dict1['t'],dict1['2'],dict1['t'],dict1['3'])