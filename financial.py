"""
Docstring for financial.py module.

This module contains functions for financial calculations in the manufacturing process.
"""


def calculate_overhead(manufacturing_cost, est_sell_price):
    """
    Calculates the overhead percentage of a manufacturing process.

    Parameters
    -----------
    manufacturing_cost: int or float
        The total cost of the manufacturing process.
    est_sell_price: int or float
        Estimated selling price of the items produced.

    Returns
    ----------
    overheadRounded: int
        Overhead percentage rounded to integer.

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
            overhead = (1 - (manufacturing_cost / est_sell_price)) * 100
            overheadRounded = round(overhead)
            return overheadRounded

    else:
        raise ValueError('You had negative numbers in your income numbers.')


MANUFACTURING_COST = 4000000
ESTIMATED_SELLING_PRICE = 5780000

print(calculate_overhead(MANUFACTURING_COST, ESTIMATED_SELLING_PRICE))
