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
Enter starting savings account balance: [user_input]
Enter account interest rate: [user_input]
Enter months to maturity: [user_input]
```
User entry will be checked as follows:
1. The user has entered a value for the prompt
2. The value is a valid number
3. For account balance and interest rate the value entered must convert to a float
4. For the months entered the value must convert to an int 

In the event invalid is provided, a warning will be provided to the user and they will be prompted for the data until a valid input is provided.

Successful entry based on the user input will be provided based on the folloing calculation 

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

### Account Class (Account.py)
The ```Account``` class provides a simple object to store account information.  This class provides a ```set``` function to store the account balance and the interest gained on the account. 

Both the ```savings_account``` and ```cd_account``` functionality utilize the ```Account``` class and the set the necessary variables.

### savings_account.py

The ```savings_account``` script provides a single function ```create_savings_account``` to perform the following:  
1. Create a new ```Account```
2. Calculate the updated account balance and accrued interest based on the data provided by the user. 
3. Sets and store the values in ```Account```


### cd_account.py

The ```cd_account``` script provides a single function ```create_cd_account``` to perform the following:  
1. Create a new ```Account```
2. Calculate the updated account balance and accrued interest based on the data provided by the user. 
3. Sets and store the values in ```Account```


