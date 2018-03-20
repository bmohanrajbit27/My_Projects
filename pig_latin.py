import sys

def pig_latin(word):
	if word[0] in ['a','e','i','o','u']:
		return word+'ay'
	else:
		return word[1:]+word[0]+'y'


print(f'The piglatin word for {sys.argv[1]} is {pig_latin(sys.argv[1])}')
