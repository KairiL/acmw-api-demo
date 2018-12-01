import time
from acmw_api_demo.types.base_class import CLASS
import random
import logging.config
#from os import path
import sys

DEBUG = True
class SlowMather(CLASS):
    def __init__(self):
        super(SlowMather, self).__init__()

        ##We could use files, but relative paths will log in the install path, not the dev path
        #use os.path because logging looks in cwd instead of script directory
        #logging.config.fileConfig(log_file_path)
        logging.StreamHandler(sys.stdout)
        self.log.setLevel('DEBUG')

        self.one=1
        self.two=2
        self.three=3

    def add(self, x: int, y: int=0):
        """
        Returns the summed value of x and y, but with more molasses
        """
        if DEBUG:
            print(f'DEBUG: x={x}')
            print(f'DEBUG: y={y}')

        self.log.debug("Entered add in slow_math Doer")

        if not self.is_legit_input(x, y, func_name='add'):
            return False

        time.sleep(5)
        return x+y

    def three_times_three(self):
        self.log.warning('This is just a test warning in three_times_three')
        self.log.debug("unittest sets logging to warning, so this debug text \
                        won't appear during test runs")
        return self.three * self.three

    def subtract(self, x: int, y: int=0):
        """
        Returns the value of x less y, but with more molasses
        """
        if not self.is_legit_input(x, y, func_name='subtract'):
            return False

        time.sleep(5)
        return x-y

    def multiply(self, x: int, y: int=1):
        """
        Adds <x> to Zero <y> times and returns it.
        Even colder molasses.
        Randomly fails because of hypothetical mainframe behavior
        """
        MAX_ATTEMPTS=25
        if not self.is_legit_input(x, y, 
                                   func_name='multiply', 
                                   force_y_no_neg=True):
            return False
        if x == 0 or y == 0:
            return 0
        time.sleep(5)
        for _ in range(MAX_ATTEMPTS):
            try:
                return self.risky_multiply(x, y)
            except EOFError:
                self.log.warning('risky_multiply failed catastrophically in multiply!')
                
        self.log.error('Reached max attempts at risky_multiply inside multiply')
        return None

    def risky_multiply(self, x: int, y: int):
        """
        Multiplies two integers without error handling.
        Sometimes fails due to totally hypothetical and definitely not super frustrating mainframe behavior
        """
        result = x*y
        if random.random() > .3:
            raise EOFError
        return result

    def x_to_the_y(self, x: int, y: int):
        """X^Y"""
        if not self.is_legit_input(x, y, 
                                   func_name='x_to_the_y', 
                                   force_y_no_neg=True):
            return False
        result = 1
        for i in range(y):
            result = self.multiply(result, x)
        return result

    def quick_divide(self, x: int, y: int=1):
        return x/y

    def is_legit_input(self, x: int, y: int, logger=None, func_name: str='', force_y_no_neg=False):
        if force_y_no_neg:
            be_a_what=' non-negative '
        else:
            be_a_what='n '

        if func_name != '':
            in_func = ' in {func_name}'
        else:
            in_func = ''

        if not isinstance(x, int):
            self.log.error(f'x must be a{be_a_what}integer{in_func}')
            self.log.error(f'x was {x}\ny was {y}')
            return False
            
        if (not isinstance(y, int)) or (force_y_no_neg and y < 0):
            self.log.error(f'y must be a{be_a_what}integer{in_func}')
            self.log.error(f'x was {x}\ny was {y}')
            return False

        return True