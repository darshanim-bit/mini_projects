import math
import random

from guess_number import GuessNumber



if __name__ == "__main__":
    

    lower_limit = int(input('Enter Lower bound Number:\n'))
    upper_limit = int(input('Enter Upper bound Number:\n'))

    guess_obj = GuessNumber(lower_bound=lower_limit,
                            upper_bound=upper_limit)

    count = 1
    rand_num = guess_obj.random_num()
    print(f'random number is {rand_num}')


    while count <= guess_obj.num_of_attempt():
        guess_num = int(input('Enter Guess Number:\n'))
        
        if lower_limit <= guess_num <= upper_limit:
            if guess_num == rand_num:
                print('Congradulations')
                print(f'you have guessed the Number {guess_num} in {count} attempts')
                break
            elif guess_num > rand_num:
                count +=1
                print('Try again! guessed number is large')
                # guess_num = int(input('Enter Guess Number:\n'))
            elif guess_num < rand_num:
                count +=1
                print('Try again! guessed number is small')
                # guess_num = int(input('Enter Guess Number:\n'))
        else:
            count += 1
            print('out of range or wrong input Try again')
            # guess_num = int(input('Enter Guess Number:\n'))
            
            
    else :
        print('acceeded the number of attempts')
                