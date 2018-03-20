from random import randint

print('''

    program that picks a random integer from 1 to 100, and has players guess the number. 

    The rules are:

    1.Please select a number between 1 and 100.
    2.If your first guess is within 10 of the computer guess, you will get a reply as 'warm'
    3.If your first guess is further 10 away from the computer guess, you will get a reply as 'cold'
    4.On all subsequent turns, if a guess is
    5.Closer to the number than the previous guess, you will get "WARMER!"
    6.Farther from the number than the previous guess, you will get "COLDER! 
    
    Once you guessed correctly, you will be congragulated with the number of attempts you took to achieve it
    ''')

comp_value = randint(1,101)
#print(comp_value)
iffirst_guess = True
guess_list = []

while True:
    
    guess = int(input('Please guess a number: '))
    
    if guess < 1 or guess > 100:
        print('Sorry out of bounds, guess from 1 to 100')
        continue
    elif guess == comp_value:
        guess_list.append(guess-comp_value)
        break
    elif abs(guess-comp_value) < 10 and iffirst_guess == True:
        print('warm')
        guess_list.append(abs(guess-comp_value))
        iffirst_guess = False
    elif abs(guess-comp_value) > 10 and iffirst_guess == True:
        print('cold')
        guess_list.append(abs(guess-comp_value))
        iffirst_guess = False
   
    elif abs(guess-comp_value) <= guess_list[-1] and iffirst_guess == False:
        guess_list.append(abs(guess-comp_value))
        #print(guess_list)
        print('warmer')
    elif abs(guess-comp_value) > guess_list[-1] and iffirst_guess == False:
        guess_list.append(abs(guess-comp_value))
        #print(guess_list)
        print('colder')

print(f'congragulation, you have successfully guessed in {len(guess_list)} attempts')
