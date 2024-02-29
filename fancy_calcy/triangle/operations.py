import math

__all__ = ["calculate_hypotenuse"]


def calculate_hypotenuse(base, height):
    """
    Calculate the hypotenuse of a right triangle.

    Parameters
    ----------
    base : float
        The length of the base of the triangle.
    height : float
        The height of the triangle.

    Returns
    -------
    float
        The length of the hypotenuse.

    Raises
    ------
    ValueError
        If base or height is not a positive number.

    Notes
    -----

    We utilize the Pythagorean theorem to calculate the hypotenuse:

        $$c = \sqrt{a^2 + b^2}$$ 

    where
        * `c` is the hypotenuse
        * `a` and `b` are the base and height of the triangle, respectively.



    Examples
    --------
    >>> from fancy_calcy.triangle import calculate_hypotenuse
    >>> calculate_hypotenuse(3, 4)
    5.0
    >>> calculate_hypotenuse(5, 12)
    13.0
    """
    if base <= 0 or height <= 0:
        raise ValueError("Base and height must be positive numbers.")

    return math.sqrt(base**2 + height**2)
