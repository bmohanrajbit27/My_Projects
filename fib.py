'''
     Fibonacci Sequence - Enter a number and have the program generate the Fibonacci sequence to that number or to the Nth number.
     sample output:
     Enter the up to number that you want produce fib series: 34
     0
     1
     1
     2
     3
     5
     8
     13
     21
     34
'''
a = 0
b = 1
up_to_num = int(input('Enter the up to number that you want produce fib series: '))
print(a)
while b <= up_to_num:
   print(b)
   a,b = b,a+b
 
