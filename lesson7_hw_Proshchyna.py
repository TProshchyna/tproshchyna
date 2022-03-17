#Task 1
#A simple function.
#Create a simple function called favorite_movie, which takes a string containing the name of your favorite movie. The function should then print “My favorite movie is named {name}”.

def favorite_movie(name):
     print(f'My favorite movie is {name}')

favorite_movie('Tinder Swindler')

#Task 2
#Creating a dictionary.
#Create a function called make_country, which takes in a country’s name and capital as parameters. Then create a dictionary from those two, with ‘name’ as a key and ‘capital’ as a parameter. Make the function print out the values of the dictionary to make sure that it works as intended.

def make_country(**kwargs):
    country_dict=kwargs
    print(f'The basic info about our country:' , country_dict)
    print(f'The capital of {country_dict["name"]} is {country_dict["capital"]}')

make_country(name='Ukraine',capital='Kyiv')

#Task 3
#A simple calculator.
#Create a function called make_operation, which takes in a simple arithmetic operator as a first parameter (to keep things simple let it only be ‘+’, ‘-’ or ‘*’) and an arbitrary number of arguments (only numbers) as the second parameter. Then return the sum or product of all the numbers in the arbitrary parameter. For example:

#the call make_operation(‘+’, 7, 7, 2) should return 16
#the call make_operation(‘-’, 5, 5, -10, -20) should return 30
#the call make_operation(‘*’, 7, 6) should return 42

def make_operation(operation,*args):
    product = args[0]
    other = args[0]
    if operation=='*':
        for a in args[1:]:
            product *= a
        return product
    elif operation=='-':
        for a in args[1:]:
            other -= a
        return other
    elif operation=='+':
        for a in args[1:]:
            other += a
        return other

print(make_operation('+', 7, 7, 2))
print(make_operation('-', 5, 5, -10, -20))
print(make_operation('*', 7, 6))


