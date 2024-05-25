"""
This module aims to highlight the S.O.L.I.D. open-close principle.
The basic version does not follow the open-close principle and therefore is to
refactor.
"""
import unittest
from statistics import mean

CUSTOMER_EXCHANGE = [
    10, -25, 30, -50, 20, 10, -20, 30
]

PREVIOUS_KNOWN_BALANCE = 100


class BankCustomer:
    """
    Bank customer class holding the basic data and methods to display customer
    information.
    """

    def __init__(self, balance: int | float) -> None:
        """
        Constructor for the BankCustomer class.
        Initialize the balance as an integer and the daily exchanges as 0.

           :param balance: Integer representing the customer's balance.
        """
        self.balance = balance
        self.sum_daily_exchanges = 0
        self.average_daily_exchanges = 0

    def display_customer_information(self, exchanges: list[int]) -> None:
        """
        Display the customer's balance and the daily exchanges in the stdout.

           :param exchanges: List of integers representing the daily exchanges.
        """
        self.sum_daily_exchanges = sum(exchanges)
        self.average_daily_exchanges = mean(exchanges)
        self.balance += self.sum_daily_exchanges
        print(f"Customer balance: {self.balance}")
        print(f"Daily exchanges: {self.sum_daily_exchanges}")
        print(f"Average daily exchanges: {self.average_daily_exchanges}")


class TestBankCustomer(unittest.TestCase):
    def test_customer_balance(self):
        """
        Instantiate a BankCustomer object and display the customer's
        information.
        """
        customer = BankCustomer(PREVIOUS_KNOWN_BALANCE)
        customer.display_customer_information(CUSTOMER_EXCHANGE)
