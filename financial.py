"""
Docstring for financial.py module.

This module contains functions for financial calculations in the manufacturing process.
"""


def calculate_turnover(manufacturing_cost, est_sell_price):
    """
    Calculates the turnover percentage of a manufacturing process.

    Parameters
    -----------
    manufacturing_cost: int or float
        The total cost of the manufacturing process.
    est_sell_price: int or float
        Estimated selling price of the items produced.

    Returns
    ----------
    turnover_rounded: int
        Turnover percentage rounded to integer.

    Raises
    ----------
    ZeroDivisionError
        If estimated selling price is 0, calculation is not possible.
    ValueError
        If selling price is negative.
    """
    if manufacturing_cost and est_sell_price >= 0:

        if est_sell_price == 0:
            raise ZeroDivisionError('Estimated selling price is 0.')
        else:
            turnover = (1 - (manufacturing_cost / est_sell_price)) * 100
            turnover_rounded = round(turnover)
            return turnover_rounded

    else:
        raise ValueError('You had negative numbers in your income numbers.')


def determine_turnover_value(turnover):
    """
    Determines the value of the turnover, if the manufacturing is profitable or not.

    Parameters
    -----------
    turnover: int or float
        The turnover percentage.

    Returns
    ----------
    str
        Returns a string defining the turnover value.

    Notes
    ----------
    Turnover values are determined with the following table:
       |   turnover < 0%     |     turnover < 15%  |     >15% turnover <40%   |      >40%  turnover   <100%    |
       ---------------------------------------------------------------------------------------------------------
       |   Negative turnover | Low turnover value  |    Good turnover value   |    Excellent turnover value.   |

    """
    if turnover < 0:
        return 'Negative turnover value.'
    elif turnover < 15:
        return 'Low turnover value.'
    elif turnover < 40:
        return 'Good turnover value.'
    elif turnover < 100:
        return 'Excellent turnover value.'


MANUFACTURING_COST = 6000000
ESTIMATED_SELLING_PRICE = 45000000

turnover = calculate_turnover(MANUFACTURING_COST, ESTIMATED_SELLING_PRICE)

print('Estimated turnover {} %'.format(turnover))

print('The value of the overhead is: {}'.format(determine_turnover_value(turnover)))


