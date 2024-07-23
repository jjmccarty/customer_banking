# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from savings_account import create_savings_account
from cd_account  import create_cd_account

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
    savings_maturity = input_as_int("Enter the months to maturity: ")
    

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
    cd_maturity = input_as_int("Enter the months to maturity: ")

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

def input_as_int(input_str):
    """Convenience call to input_as_num which explicity passes the int value

    Args:
        input_str (str): The text for the user input entry prompt.

    Returns:
        int: The user input cast to an int
    """
    return input_to_num(input_str, int)

def input_as_float(input_str):
    """Convenience call to input_as_num which explicity passes the float value

    Args:
        input_str (str): The text for the user input entry prompt.

    Returns:
        float: The user input cast to an int
    """
    return input_to_num(input_str, float)

def input_to_num(input_str, cast_type):
    """Requests a user input from the text provided and returns the input cast 
       the appropriate numerical type, either a float or int.  If the value
       cannot be converted to the type specified a warning will be issues and
       the user will be prompted for the value to be entered again.

    Args:
        input_str (str): The text for the user input entry prompt.
        cast_type (float or int): The object type to verify input against and
                cast the retun value to.

    Returns:
        float or int: The user input cast to the object type requested at 
            execution time of the function. 
    """
    input_value = ""
    while True:
        temp_value = input(input_str)
        if cast_type == int and temp_value.isdigit():
            #check this value can be cast to an int 
            input_value = int(temp_value)
            break
        if cast_type == float and temp_value.strip().replace(".","").isdigit():
            #check this value can be cast to a float
            input_value = float(temp_value)
            break
        else:
            #otherwise input is invalid, warn and reprompt entry
            print(f"The value entered {temp_value} is not a valid number")

    return input_value

if __name__ == "__main__":
    # Call the main function.
    print("customer_banking.py")
    main()
