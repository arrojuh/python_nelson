## String Indexing and Slicing

word = "harikrishna"
word1 ='12=92f9ua!@#$'
number = 1234556798
num_str = "1234556798"

#() ## when we give something to the function/object
num_str[1] # when we ask something from the function/object

# POSITIVE INDEX --0 123456---
# NEGATIVE INDEX --0 -5-4-3-2-1

print(word[0],word[-1])

# syntax--> string[start:end]

word[0:4] # positive

word[-5:-1] # negative # Python omits the right index

word[-5:] # no number means till end/start
word[:5]

# syntax--> string[start:end:step]
#start+step, start+step+step
word[0:7:1] #0,0+1,0+1+1,0+1+1+1,0+1+1+1+1..7
word[0:7:2] #0,0+2,0+2+2,0+2+2+2..
word[-7:-1] # Krishn
#h a  r i k r i s h n a
#0-10-9-8-7-6-5-4-3-2-1
word[-7:-1]
word[-7::-1]#-7,-7-1,-7-1-1,-7-1-1-1

word[::-1] # reverses a string

