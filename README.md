# customer_banking (Python-challenge-2)

Basic request for a simple banking system which will ask a user for the starting balance, account interest rate, and months of interest for a savings account and a CD account.  

The system will calculate the new balance and the amout of the interest accrued and print that to the user. 

## Program Execution (customer_banking.py)

Program execution begins by executing the customer_banking.py script from a 
python environment

```
python customer_banking.py
```

The system will request 3 inputs from the user for the savings account and the CD account beginning with the savings account.  For example:

```
Enter starting savings account balance: [user_input as float]
Enter account interest rate: [user_input as float]
Enter months to maturity: [user_input as int]
```
User entry will be checked as follows:
1. The user has entered a value for the prompt
2. The value is a valid number
3. For account balance and interest rate the value entered must convert to a float
4. For the months entered the value must convert to an int 

In the event invalid is provided, a warning will be provided to the user and they will be prompted for the data until a valid input is provided.

The system will output the new balance (starting balance + interested earned) as well as the interest earned on the account for the months specifed.

Calculation of the interest earned is based on the homework hint provided as follows

**interest_earned = balance * (interest_rate/100 * months/12)**

```
UPDATED SAVINGS INFORMATION
----------------------------------------
Updated Balance: $209.45
Interest earned over 12 months is $5.11
----------------------------------------
```

## Code structures

### Main program
Initial code invocation happens when the ```customer_banking.py``` script is executed.  This will run the ```main()``` function to request user input as described in the program execution section of this README.

The main function:  
1.  Invokes the ```create_savings_account``` and ```create_cd_account``` functions with the user input provided.  (User input is checked for argument type prior to invocation of these functions)
2.   Outputs the result of the function invocation with the updated account balance and calculated interest amount to the screen.

### savings_account.py

The ```savings_account``` script provides a single function ```create_savings_account``` to perform the following: 

1. Calculates the updated account balance and accrued interest based on the arguments provided.
2. Sets and store the values in an ```Account``` object
3. Returns the updated account balance and interest dollars received

> Note: Parts of the ```create_savings_account``` logic as defined in homework instructions was duplicative to the logic for the ```create_cd_account``` function from the ```cd_account.py``` file.  To eliminate the duplication this was refactored into a method on the ```Account``` class which is invoked from these functions.

### cd_account.py

The ```cd_account``` script provides a single function ```create_cd_account``` to perform the following:  

1. Calculate the updated cd account balance and accrued interest based on the arguments provided. 
2. Sets and store the values in an ```Account``` object
3. Returns the updated account balance and interest dollars received

> Please see note under ```savings_account.py``` for relevant refactoring details.

### Account Class (Account.py)
The ```Account``` class provides a simple object to store account information.  This class provides a ```set``` function to store the account balance and the interest gained on the account. 

The ```Account``` class also contains a new method called ```update_balance_with_interest``` refactored from the original logic specified in the homework instructions for ```create_savings_account``` and ```create_cd_account``` to reduce duplicative code.  The function will add the accrued interest to the account balance based on the interest rate and months provided. 

### BankingUtils Module (BankingUtils.py)
The BankingUtils module contains basic utility functions to validate user input as a specific data type (int or float) and return that input value cast to the correct type. 

This was added to the code and imported by the ```customer_banking.py``` script to simplify the code in the main script execution.  
