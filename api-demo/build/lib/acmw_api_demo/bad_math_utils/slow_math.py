import time
from acmw_api_demo.types.base_class import CLASS
import random

class SlowMather(CLASS):
    def add(self, x: int, y: int=0):
        """
        Returns the summed value of x and y, but with more molasses
        """

        self.log.debug("Entered add in slow_math Doer")

        if not self.is_legit_input(x, y, func_name='add'):
            return False

        time.sleep(5)
        return x+y

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
        MAX_ATTEMPTS=4
        if not self.is_legit_input(x, y, 
                                   func_name='multiply', 
                                   force_y_pos=True):
            return False

        for _ in range(MAX_ATTEMPTS):
            try:
                return self.risky_multiply(x, y), True
            except EOFError:
                self.log.warning('risky_multiply failed catastrophically in multiply!')
                
        self.log.error('Reached max attempts at risky_multiply inside multiply')
        return None

    def risky_multiply(self, x: int, y: int):
        """
        Multiplies two integers without error handling.
        Sometimes fails due to totally hypothetical and definitely not super frustrating mainframe behavior
        """
        result = 0
        for _ in range(y):
            result += self.add(x, result)
        if random.randint > .95:
            raise EOFError
        return result

    def x_to_the_y(self, x: int, y: int):
        """X^Y"""
        if not self.is_legit_input(x, y, 
                                   func_name='x_to_the_y', 
                                   force_y_pos=True):
            return False
        result = 1
        for i in range(y):
            result = self.multiply(result, x)
        return result

    def divide(self, x: int, y: int=1):
        pass

    def is_legit_input(self, x: int, y: int, logger=None, func_name: str='', force_y_pos=False):
        if force_y_pos:
            be_a_what=' non-negative '
        else:
            be_a_what='n '
        if func_name != '':
            in_func = ' in {func_name}'
        else:
            in_func = ''
        if not isinstance(x, int):
            self.log.error(f'x must be a{be_a_what}integer{in_func}')
            return False
        if (not isinstance(y, int)) or (force_y_pos and y < 0):
            self.log.error(f'y must be a{be_a_what}integer{in_func}')
            return False