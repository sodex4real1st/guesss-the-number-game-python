import random
"""this python code generate random number and as the user to input any number within the range of 1 - 10.
if the number generated is higer than the number input, this code will tell the user number too low
and if the number generated is lower than the number input, this code will tell the user number too high"""

user_number= int(input('what your guesss ')) # ask user for their guess


random_number = random.randint(1,11) # get random number with random.randint functio



while user_number != random_number: # to check if user guess is not equal to computer guess

    if user_number > random_number:  #check if the user guess is greater than computer guess
        print('your guess is too high') # notify the user that guess is too high
        user_number= int(input('try again:- ')) # ask user to try again


    elif user_number < random_number: # check if the user guess is less than computer guess
        print('your guess is too low')  # notify the user that guess is too low
        user_number= int(input('try again:- ')) # ask user to try again


    else:  # last statement if both of the above condition false
        break  # breaks out of the loop

print('your guess is right')  #tell user the guss is right

