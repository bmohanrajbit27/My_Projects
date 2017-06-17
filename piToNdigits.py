'''
    we all know value of pi is approximately 3.14 but the exact value is 3.142857142857142793701541449991054832935333251953125
    phew good brains needed to memorize that.
    This script will take the input of how many decimal digits you wanted to display on the output.
    I saved this script as piToNdigits.
    
    python piToNdigits.py 5 
    3.14286
    
    change the value and see the output.
    
    HAVE FUN...


'''
import sys
user_input = int(sys.argv[1])
pi = float(22)/7
a = '{'+':'+'.'+ str(user_input)+'f'+'}'
if user_input <= 51:
  print(a.format(pi))
elif user_input > 51:
  a = '{'+':'+'.'+ str(51)+'f'+'}'
  print('There are only 51 decimal places for value of pi')
  print(a.format(pi))
