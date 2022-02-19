##Task 1

import random
while True:
    choice=input('Do u want to play the game? Enter yes or no: ')
    while choice=='yes':
        try:
            number = random.randint(1, 10)
            guess=int(input('Lets start, guess an integer between 1 and 10. What is your guess?: '))
            if guess==number:
                print('Good job! You are right')
                break
            elif guess!=number:
                print('You are wrong')
                break
        except ValueError:
            print('Please enter only integers between 1 and 10')
            break
    else:
        if choice=='no':
            break
        else:
            print('Please, enter yes or no')
            continue

##Task 2

while True:
    print('Hi! This is a birthday greeting program')
    try:
        name=input('Please, type your name here: ')
        age=int(input('Please, type your age here: '))
        new_age=age+1
        print(f'Hello {name}, on your next birthday you’ll be {new_age} years')
        break
    except ValueError:
        print('Your age should be an integer. Please, try again')
        continue

##Task 3

import random
word=input('Please, enter a word: ')
print(f'Here is 5 random words from all letters of {word}')
count=0
list=[i for i in word]

while count<5:
    random.shuffle(list)
    new_string=''
    for i in list:
        new_string+=i
    print(new_string)
    count+=1

#Task 4

while True:
    try:
        expression=int(input('Lets start, what is the answer of this expression: (5+7)*11 '))
        if expression==(5+7)*11:
            print('Good job! You are right')
            break
        else:
            print('You are wrong. Lets try again')
            continue
    except ValueError:
            print('Please enter only integers as answer')
            continue

