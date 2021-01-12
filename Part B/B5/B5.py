import sys 
import os
from functools import reduce

if(len(sys.argv)!=2):
    print('\nInvalid arguments!')
    sys.exit()

if(not(os.path.exists(sys.argv[1]))):
    print('\nFile does not exist!')
    sys.exit()

if(sys.argv[1].split('.')[-1]!='txt'):
    print('\nOnly .txt files supported')
    sys.exit()

dict = {}

with open(sys.argv[1]) as f:
    for line in f:
        for word in line.split():
            dict[word] = dict.get(word,0) + 1

sorted_words = sorted( dict.items(), key = lambda item: item[1], reverse = True  )

wordLen=[]
for i in range(10):
    try:
        wordTuple = sorted_words[i]
        wordLen.append(len(wordTuple[0]))
        print(f'\nThe word is {wordTuple[0]}, length is {wordLen[-1]} and freqency is {wordTuple[1]}')
    except IndexError:
        print('\nDocument contains less than 10 unique words')
        break


print ("Lengths of 10 most frequently occuring words:")
print (wordLen)


sum = reduce( lambda x,y: x+y, wordLen)
print ("Average length of words: " , sum/len(wordLen))


squares = [x**2 for x in wordLen if x%2 != 0]
print ("Squares of odd word lengths: ")
print (squares)

