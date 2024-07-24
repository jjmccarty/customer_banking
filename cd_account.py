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

    # Checking argument type in case type was not checked at invocation
    if type(balance) != float or type(interest_rate) != float or type(months) != int: 
        print("INVALID ARGUEMENT TYPE: ")
        print(f"Expected create_cd_account(float, float, int)")
        print(f"Recieved create_cd_account({type(balance)}, {type(interest_rate)}, {type(months)})")
        print("The system will now exit")
        exit()

    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # Interest hasn't been calculated yet so we are passing 0 for now.
    cd_account = Account(balance, 0)

    # Note: original instructions had the calculation for updating the balance
    # directly in this script, however it is same logic for the savings_account
    # and the cd_account script.  Moved to an Account method to reduce duplication
    cd_account.update_balance_with_interest(interest_rate, months)
    
    # Return the updated balance and interest earned.
    return  cd_account.balance, cd_account.interest

if __name__ == "__main__":
    # Only runs when cd_account.py is directly executed.  
    # Used for validation/testing of functions outside of the main program.
    print("Executing script cd_account.py") 
    cd_account_info =  create_cd_account(100.00, .5, 12)
    print(f"CD Account info: {cd_account_info}")

    #uncomment for create_savings_account parameter type check
    #cd_account_info = create_cd_account("100.00", .5, 12)
