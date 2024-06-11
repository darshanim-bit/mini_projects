import math
import random

class GuessNumber:
    
    def __init__(self,lower_bound,upper_bound) -> None:
        assert isinstance(lower_bound,int), 'please enter intiger number'
        assert isinstance(upper_bound, int), 'please enter intiger number'
        
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.__rand_num = self.random_num()
        
        
    def random_num(self):
        return random.randint(self.lower_bound,self.upper_bound)
        
    def num_of_attempt(self):
        
        attempts = math.log(self.upper_bound-self.lower_bound+1,2)
        return attempts
    
    def guess_result(self,num):
        
        if num == self.__rand_num:
            print('Congradulations')
        elif num > self.__rand_num:
            print('Try again! guessed number is large')
        elif num < self.__rand_num:
            print('Try again! guessed number is small')
            
    
        
    
        
        
        
        
        
        
        
        
        
        


if __name__ == '__main__':
    
    print(GuessNumber(1,20).lower_bound)
