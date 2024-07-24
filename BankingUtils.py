# Basic utilies for the customer_banking system to assist in conversion of user
# input to a specific type (float or int)

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

def input_as_int(input_str):
    """
    Convenience call to input_as_num which explicity passes the int value
    This is probably overkill for a simple verification routine, but does allow
    for additional int specific rules at a later time.

    Args:
        input_str (str): The text for the user input entry prompt.

    Returns:
        int: The user input cast to an int
    """
    return input_to_num(input_str, int)

def input_as_float(input_str):
    """
    Convenience call to input_as_num which explicity passes the float value
    This is probably overkill for a simple verification routine, but does allow
    for additional float specific rules at a later time. 

    Args:
        input_str (str): The text for the user input entry prompt.

    Returns:
        float: The user input cast to an int
    """
    return input_to_num(input_str, float)