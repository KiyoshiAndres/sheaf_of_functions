class object_function():
    def __init__(self, function):
        self.base_function = function

    def __call__(self, *args):
        return self.base_function(*args)

    def __add__(self, other):
        """magic method to add two functions"""
        def addition(*args):
            return self.base_function(*args) + other.base_function(*args)
        sum_of_functions = object_function(addition)
        sum_of_functions.base_function = addition
        return sum_of_functions

    def __sub__(self, other):
        """magic method to subtract two functions"""
        def subtraction(*args):
            return self.base_function(*args) - other.base_function(*args)
        difference_of_functions = object_function(subtraction)
        difference_of_functions.base_function = subtraction
        return difference_of_functions

    def __mul__(self, other):
        """magic method to multiply two functions, or scalar product"""

        if type(other) == int or type(other) == float:
            def multiplication(*args):
                return self.base_function(*args) * other
            product_of_functions = object_function(multiplication)
            return product_of_functions

        def multiplication(*args):
            return self.base_function(*args) * other.base_function(*args)
        product_of_functions = object_function(multiplication)
        return product_of_functions

# Testing

def square_function(variable):
    return variable ** 2
x_squared = object_function(square_function)
two_x_squared = x_squared * 2
print(two_x_squared(5))
