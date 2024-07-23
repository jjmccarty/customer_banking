# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from savings_account import create_savings_account
from cd_account  import create_cd_account

def input_to_num(input_str, cast_type):
    print("validate")
    input_value = ""
    while True:
        isBreak = False
        temp_value = input(input_str)
        print(f"User Entered: {temp_value}")   
        if(cast_type == int) and temp_value.isdigit():
            input_value = int(temp_value)
            break
        if(cast_type == float and 
           (temp_value.strip().replace(".","") == float or temp_value.isdigit())):
            input_value = float(temp_value)
            break
        else:
            print(f"The value entered {temp_value} is not a valid number")

    print(f"Returning {input_value} of {type(input_value)}")
    return input_value

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE

    savings_balance = input_to_num("Enter starting savings account balance: ", float)
    savings_interest = input_to_num("Enter the account interest rate: ", float)
    savings_maturity = input_to_num("Enter the months to maturity: ", int)
    

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE

    # Call the create_cd_account function and pass the variables from the user.
    #updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE

if __name__ == "__main__":
    # Call the main function.
    print("customer_banking.py")
    main()
