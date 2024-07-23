"""Import the Account class from the Account.py file."""
# ADD YOUR CODE HERE
from Account import Account

# Define a function for the Savings Account
def create_savings_account(balance, interest_rate, months):
    """Creates a savings account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding interest earned.
        float: The interest dollars earned.
    """

    # Checking argument type in case type was not checked at invocation
    if type(balance) != float or type(interest_rate) != float or type(months) != int: 
        print("INVALID ARGUMENT TYPE: ")
        print(f"Expected create_savings_account(float, float, int)")
        print(f"Recieved create_savings_account({type(balance)}, {type(interest_rate)}, {type(months)})")
        print("The system will now exit")
        exit()

    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # Interest hasn't been calculated yet so we are passing 0 for now
    # ADD YOUR CODE HERE
    account = Account(balance, 0)

    # Calculate interest earned
    # provided from homework hint
    interest_earned = balance * (interest_rate/100 * months/12)
    interest_earned = round(interest_earned, 2)

    # Update the savings account balance by adding the interest earned
    balance = balance + interest_earned
    balance = round(balance, 2)

    # Pass the updated_balance to the set balance method using the instance of the SavingsAccount class.
    account.set_balance(balance)

    # Pass the interest_earned to the set interest method using the instance of the SavingsAccount class.
    account.set_interest(interest_earned)

    # Return the updated balance and interest earned.
    return  balance, interest_earned

if __name__ == "__main__":
    # Only runs when savings_account.py is directly executed.  
    # Used for validation/testing of functions outside of the main program.
    print("Executing script savings_account.py") 
    account_info = create_savings_account(100.00, 2.5, 12)    
    print(f"Account info: {account_info}")

    #uncomment for create_savings_account parameter type check
    #account_info = create_savings_account("100.00", 2.5, 12)