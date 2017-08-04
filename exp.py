'''
        math module in python has numerous helful functions and one such function is exp. Below source code accepts an integer from user 
        and generate e up to that many decimal places 
        
        sample output:
        Enter the decimal value lenght: 45
        2.718281828459045090795598298427648842334747314
        
        Enter the decimal value lenght: 67
        only 50 decimal places are allowed
        2.71828182845904509079559829842764884233474731445312
'''

d_l = int(input('Enter the decimal value lenght: '))
e = 2.718281828459045

def func(d_l):
    st = '{'+':'+'.'+str(d_l)+'f'+'}'
    return st

if d_l <=50:
    print(func(d_l).format(e))
else:
    d_l = 50
    print('only 50 decimal places are allowed')
    print(func(d_l).format(e))

