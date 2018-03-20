import sys

def myfunc(word):
    neword=''
    for index,value in enumerate(word):
        if index%2 == 0:
            neword += value.lower()
        else:
            neword += value.upper()
    return neword
    
result = myfunc(sys.arg[1])
print(f'The word changed from {sys.argv[1]} to {result}')
