

__all__ = ["BasicOperations"]


class BasicOperations:
    """
    A class that performs basic arithmetic operations on two numbers.

    Parameters
    ----------
    num1 : int or float
        The first number.
    num2 : int or float
        The second number.


    Raises
    ------
    AssertionError
        If `num1` or `num2` is not a number.


    See Also
    --------
    :func:`fancy_calcy.triangle.calculate_hypotenuse`


    Examples
    --------
    >>> from fancy_calcy.basics import BasicOperations
    >>> calc = BasicOperations(5, 3)
    >>> calc.add()  
    8
    >>> calc.subtract()
    2
    >>> calc.multiply() 
    15
    >>> calc.divide()
    1.6666666666666667
    >>> calc.integer_divide()
    1
    """

    def __init__(self, num1, num2):
        """
        Initialize SimpleOperations object with two numbers.

        Parameters:
        num1 (int or float): The first number.
        num2 (int or float): The second number.

        Raises:
        AssertionError: If num1 or num2 is not a number.
        """
        self.num1 = num1
        self.num2 = num2

        assert isinstance(self.num1, (int, float)), "num1 must be a number"
        assert isinstance(self.num2, (int, float)), "num2 must be a number"

    def add(self):
        """
        Add the two numbers.

        Returns:
        float: The sum of the two numbers.
        """
        return self.num1 + self.num2

    def subtract(self):
        """
        Subtract the second number from the first number.

        Returns:
        float: The difference between the two numbers.
        """
        return self.num1 - self.num2

    def multiply(self):
        """
        Multiply the two numbers.

        Returns:
        float: The product of the two numbers.
        """
        return self.num1 * self.num2

    def divide(self):
        """
        Divide the first number by the second number.

        Returns:
        float: The quotient of the two numbers.
        """
        return self.num1 / self.num2

    def add(self):
        """
        Add two numbers.

        Returns
        -------
        float
            The result of addition.
        """
        return self.num1 + self.num2

    def subtract(self):
        """
        Subtract the second number from the first number.

        Returns:
            int: The result of the subtraction.
        """
        return self.num1 - self.num2

    def multiply(self):
        """
        Multiply the two numbers.

        Returns:
            int: The product of `num1` and `num2`.
        """
        return self.num1 * self.num2

    def divide(self):
        """
        Divide the first number by the second number.

        Returns:
            float: The result of the division.

        Raises:
            ZeroDivisionError: If the second number is zero.
        """
        if self.num2 == 0:
            raise ZeroDivisionError("Division by zero")
        return self.num1 / self.num2

    def integer_divide(self):
        """
        Perform integer division between two numbers.

        Returns:
            int: The result of the integer division.

        Raises:
            ZeroDivisionError: If the second number is zero.
        """
        if self.num2 == 0:
            raise ZeroDivisionError("Division by zero")
        return self.num1 // self.num2
