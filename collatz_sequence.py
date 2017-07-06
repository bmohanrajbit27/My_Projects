'''
    Below script produce Collatz sequence for a given number. 
    Whatever the positive number you give as input, the script will keep on printing numbers untill it reaches value 1.
    
    HAVE FUN
'''

def return_value(number):
    if number % 2 == 0:
        value = number//2
        print(value)
        return value
    else:
        value = 3*number+1
        print(value)
        return value

number = int(input('Type an integer for producing collatz sequence: '))

while True:
    returned_value = return_value(number)
    if returned_value != 1:
        number = returned_value
    else:
        print('Thats the collatz sequence for the given number.')
        break
