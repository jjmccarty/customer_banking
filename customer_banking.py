# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from savings_account import create_savings_account
from cd_account  import create_cd_account

#moved general type checks for user input to separate module to simplify code
from BankingUtils import input_as_float, input_as_int

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    formatting_chars = 40
    formatting_divider = "-"
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE

    savings_balance = input_as_float("Enter starting savings account balance: ")
    savings_interest = input_as_float("Enter the account interest rate: ")
    savings_maturity = input_as_int("Enter the months of interest to calculate: ")
    

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(formatting_divider * formatting_chars)
    print("UPDATED SAVINGS INFORMATION")
    print(formatting_divider * formatting_chars)

    print(f"Updated Balance: ${updated_savings_balance :.2f}")
    print(f"Interest earned over {savings_maturity} months is ${interest_earned :.2f}")

    print(formatting_divider * formatting_chars)

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    cd_balance = input_as_float("Enter starting CD account balance: ")
    cd_interest = input_as_float("Enter CD account interest rate: ")
    cd_maturity = input_as_int("Enter the months of interest to calculate: ")

    # Call the create_cd_account function and pass the variables from the user. 
    updated_cd_balance, cd_interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)
    
    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(formatting_divider * formatting_chars)
    print("UPDATED CD INFORMATION")
    print(formatting_divider * formatting_chars)

    print(f"Updated CD Balance: ${updated_cd_balance :.2f}")
    print(f"Interest earned over {cd_maturity} months is ${cd_interest_earned :.2f}")

    print(formatting_divider * formatting_chars)

if __name__ == "__main__":
    # Call the main function.
    main()
