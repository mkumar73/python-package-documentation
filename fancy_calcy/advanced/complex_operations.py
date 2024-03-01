import math

__all__ = ["ScientificFunctions"]


class ScientificFunctions:
    """
    A class that provides various scientific functions.

    Note
    ----
    Just illustrating how maths equation can be added in the Python docstrings.

    - Factorial: 

    .. math::

        n! = \prod_{i=1}^{n} i = n * (n-1) * (n-2) * \dots * 1

    Where `n` is a non-negative integer.

    - Power: :math:`x^y`



    See Also
    --------
    :class:`fancy_calcy.basics.BasicOperations`


    Examples
    --------
    >>> from fancy_calcy.advanced import ScientificFunctions
    >>> sf = ScientificFunctions()
    >>> sf.factorial(5)
    120
    >>> sf.power(2, 3)
    8.0
    >>> sf.logarithm(10, 100)
    2.0
    >>> sf.sine(45)
    0.7071067811865476
    >>> sf.cosine(60)
    0.5000000000000001
    >>> sf.tangent(30)
    0.5773502691896257
    >>> sf.add_complex(2+3j, 4+5j)
    (6+8j)
    >>> sf.subtract_complex(4+5j, 2+3j)
    (2+2j)
    """

    def factorial(self, num):
        """
        Calculate the factorial of a non-negative integer.

        Parameters
        ----------
        num : int
            The number for which factorial needs to be calculated.

        Returns
        -------
        int
            The factorial of the given number.

        Raises
        ------
        ValueError
            If the number is negative.
        """
        if num < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        if num == 0:
            return 1
        else:
            result = 1
            for i in range(1, num + 1):
                result *= i
            return result

    def power(self, base, exponent):
        """
        Calculate the power of a number.

        Parameters
        ----------
        base : float
            The base number.
        exponent : float
            The exponent.

        Returns
        -------
        float
            The result of raising the base to the exponent.
        """
        return math.pow(base, exponent)

    def logarithm(self, base, num):
        """
        Calculate the logarithm of a number with a given base.

        Parameters
        ----------
        base : float
            The base of the logarithm.
        num : float
            The number for which logarithm needs to be calculated.

        Returns
        -------
        float
            The logarithm of the given number with the specified base.

        Raises
        ------
        ValueError
            If the base is 1 or if the number is non-positive.
        """
        if base == 1:
            raise ValueError("Logarithm with base 1 is not defined")
        if num <= 0:
            raise ValueError(
                "Logarithm is not defined for non-positive numbers")
        return math.log(num, base)

    def sine(self, angle):
        """
        Calculate the sine of an angle in degrees.

        Parameters
        ----------
        angle : float
            The angle in degrees.

        Returns
        -------
        float
            The sine of the given angle.
        """
        return math.sin(math.radians(angle))

    def cosine(self, angle):
        """
        Calculate the cosine of an angle in degrees.

        Parameters
        ----------
        angle : float
            The angle in degrees.

        Returns
        -------
        float
            The cosine of the given angle.
        """
        return math.cos(math.radians(angle))

    def tangent(self, angle):
        """
        Calculate the tangent of an angle in degrees.

        Parameters
        ----------
        angle : float
            The angle in degrees.

        Returns
        -------
        float
            The tangent of the given angle.

        Raises
        ------
        ZeroDivisionError
            If the angle is 90 degrees or its multiples.
        """
        if math.cos(math.radians(angle)) == 0:
            raise ZeroDivisionError(
                "Tangent is not defined at 90 degrees and its multiples")
        return math.tan(math.radians(angle))

    def add_complex(self, num1, num2):
        """
        Add two complex numbers.

        Parameters
        ----------
        num1 : complex
            The first complex number.
        num2 : complex
            The second complex number.

        Returns
        -------
        complex
            The sum of the two complex numbers.
        """
        real_part = num1.real + num2.real
        imaginary_part = num1.imag + num2.imag
        return complex(real_part, imaginary_part)

    def subtract_complex(self, num1, num2):
        """
        Subtract two complex numbers.

        Parameters
        ----------
        num1 : complex
            The first complex number.
        num2 : complex
            The second complex number.

        Returns
        -------
        complex
            The difference between the two complex numbers.
        """
        real_part = num1.real - num2.real
        imaginary_part = num1.imag - num2.imag
        return complex(real_part, imaginary_part)
