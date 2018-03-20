from random import randint

comp_value = randint(1,101)
print(comp_value)
iffirst_guess = True
guess_list = []

while True:
    
    guess = int(input('Please guess a number: '))
    
    if guess == comp_value:
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
   
    elif abs(guess-comp_value) < guess_list[-1] and iffirst_guess == False:
        guess_list.append(abs(guess-comp_value))
        #print(guess_list)
        print('warmer')
    elif abs(guess-comp_value) > guess_list[-1] and iffirst_guess == False:
        guess_list.append(abs(guess-comp_value))
        #print(guess_list)
        print('colder')

print(f'congragulation, you have successfully guessed in {len(guess_list)} attempts')
