"""Import the Account class from the Account.py file."""
from Account import Account

def create_cd_account(balance, interest_rate, months):
    """Creates a CD account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial CD account balance.
        interest_rate (float): The APR interest rate for the CD account.
        months (int): The length of months for the CD.

    Returns:
        float: The updated CD account balance after adding the interest earned.
        float: The interest dollars earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # Interest hasn't been calculated yet so we are passing 0 for now.
    cd_account = Account(balance, 0)

    # Calculate interest earned
    # provided from homework hint
    interest_earned = balance * (interest_rate/100 * months/12)
    interest_earned = round(interest_earned, 2)

    # Update the CD account balance by adding the interest earned
    balance = balance + interest_earned
    balance = round(interest_earned, 2)

    # Pass the updated_balance to the set balance method using the instance of the CDAccount class.
    cd_account.set_balance(balance)

    # Pass the interest_earned to the set interest method using the instance of the CDAccount class.
    cd_account.set_interest(interest_earned)

    # Return the updated balance and interest earned.
    return  balance, interest_earned

if __name__ == "__main__":
    # Only runs when cd_account.py is directly executed.  
    # Used for validation/testing of functions outside of the main program.
    print("Executing script cd_account.py") 
    cd_account_info =  create_cd_account(100.00, .5, 12)
    print(f"CD Account info: {cd_account_info}")
