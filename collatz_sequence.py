'''
    Below script produce Collatz sequence for a given number. 
    Whatever the positive number you give as input, the script will keep on printing numbers untill it reaches value 1.
    Sample Output:
    Type an integer for producing collatz sequence: 34
    17
    52
    26
    13
    40
    20
    10
    5
    16
    8
    4
    2
    1
    Thats the collatz sequence for the given number.
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

value_check = True
while value_check:
    try:
        number = int(input('Type an integer for producing collatz sequence: '))
        value_check = False
    except ValueError:
        print('Please enter valid number..')

while True:
    returned_value = return_value(number)
    if returned_value != 1:
        number = returned_value
    else:
        print('Thats the collatz sequence for the given number.')
        break
