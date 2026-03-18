"""
A collection of simple math operations.

This module contains basic arithmetic functions and simple polynomial functions.

"""


def simple_add(a, b):

    """
    Add two numbers.

    Parameters
    ----------
    a : int or float
        First number.
    b : int or float
        Second number.

    Returns
    -------
    int or float
        The sum of a and b.

    Examples
    --------
    >>> simple_add(2, 3)
    5
    """
    return a + b


def simple_sub(a, b):
    """
    Subtract one number from another.

    Parameters
    ----------
    a : int or float
        Number to subtract from.
    b : int or float
        Number to subtract.

    Returns
    -------
    int or float
        The result of a - b.

    Examples
    --------
    >>> simple_sub(5, 2)
    3
    """
    return a - b


def simple_mult(a, b):
    """
    Multiply two numbers.

    Parameters
    ----------
    a : int or float
        First factor.
    b : int or float
        Second factor.

    Returns
    -------
    int or float
        The product of a and b.

    Examples
    --------
    >>> simple_mult(4, 3)
    12
    """
    return a * b


def simple_div(a, b):
    """
    Divide one number by another.

    Parameters
    ----------
    a : int or float
        Numerator.
    b : int or float
        Denominator.

    Returns
    -------
    float
        The result of a / b.

    Examples
    --------
    >>> simple_div(8, 2)
    4.0
    """
    return a / b


def poly_first(x, a0, a1):
    """
    Evaluate a first degree polynomial.

    The polynomial is defined as:

    .. math::

       a_0 + a_1 x

    Parameters
    ----------
    x : int or float
        Input value.
    a0 : int or float
        Constant coefficient.
    a1 : int or float
        Linear coefficient.

    Returns
    -------
    int or float
        The value of the polynomial at x.

    Examples
    --------
    >>> poly_first(2, 1, 3)
    7
    """
    return a0 + a1 * x


def poly_second(x, a0, a1, a2):
    """
    Evaluate a second degree polynomial.

    The polynomial is defined as:

    .. math::

       a_0 + a_1 x + a_2 x^2

    Parameters
    ----------
    x : int or float
        Input value.
    a0 : int or float
        Constant coefficient.
    a1 : int or float
        Linear coefficient.
    a2 : int or float
        Quadratic coefficient.

    Returns
    -------
    int or float
        The value of the polynomial at x.

    Examples
    --------
    >>> poly_second(2, 1, 3, 4)
    23
    """
    return poly_first(x, a0, a1) + a2 * (x ** 2)


