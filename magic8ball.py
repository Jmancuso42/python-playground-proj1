#8 ball exercise
import random


eightball = ['Decidely So', 'NOPE', 'I gotta think about it a lot', 
             'For sure',
             'Think Harder',
             'Definitely not',
             'Not looking good for you',
             'this is looking pretty hazy',
             'My thinking is no way, dood',
             'Definitely',
             'The stars will align'
             ]


print(eightball[random.randint(0,len(eightball)-1)]) #pick a random int from zero to the length of the list 