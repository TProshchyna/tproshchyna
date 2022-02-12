##Task 1

name='Tetiana'
from datetime import date
import calendar
day=calendar.day_name[date.today().weekday()]

print(f'Good day {name}! {day} is a perfect day to learn some python.')
print('Good day {0}! {1} is a perfect day to learn some python.'.format(name, day))
print('Good day %s! %s is a perfect day to learn some python.' % (name, day))

##Task 2

name='Tetiana'
surname='Proshchyna'
full_name=name+' '+surname
print(f'Good day {full_name}!')

##Task 3

a=int(input('Please, enter an a:'))
b=int(input('Please, enter a b:'))

addition=a+b
subtraction=a-b
division=round(a/b,1)
multiplication=a*b
power=a**b
modulus=a % b
floor_division=a // b

print(f'The sum of {a} and {b} is {addition}')
print(f'The difference between {a} and {b} equals {subtraction}')
print(f'{a}/{b} equals {division}')
print(f'{a}*{b} equals {multiplication}')
print(f'{a} to the power of {b} equals {power}')
print(f'{a}%{b} equals {modulus}')
print(f'The floor division {a}//{b} equals {floor_division}')