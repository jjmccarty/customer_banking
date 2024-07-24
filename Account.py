""" Create a Account class with methods"""

class Account:
    """Creating an Account class with methods"""
    def __init__(self, balance, interest):
        self.balance = balance
        self.interest = interest

    # This method sets the balance of the account.
    def set_balance(self, balance):
        """Sets the balance for the for the account"""
        self.balance = balance

    # The method sets the interest gained for the account.
    def set_interest(self, interest):
        """Sets the interest gained for the the account"""
        self.interest = interest

    # Note: functionality was refactored into Account from original instructions
    # to put in savings_account and cd_account scripts to reduce duplication.
    def update_balance_with_interest(self, interest_rate, months):
        """
        Updates the account balance with additional interest accrued for the 
        specified months at the rate given.

        Args:
            interest_rate (float): The APR interest rate for the savings account.
            months (int): The length of months to determine the amount of interest.

        Returns:
        """
        # Calculate interest earned
        # provided from homework hint
        interest_earned = self.balance * (interest_rate/100 * months/12)
        interest_earned = round(interest_earned, 2)

        # Update the savings account balance by adding the interest earned
        temp_balance = self.balance + interest_earned
        temp_balance = round(temp_balance, 2)

        # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
        self.set_balance(temp_balance)

        # Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
        self.set_interest(interest_earned)