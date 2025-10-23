# Instructions

## Scenario

You are asked to design a Smart Banking Management System for a bank named “PyBank”.
The system should allow customers to open accounts, deposit or withdraw money, and the bank staff to manage various account types like Savings, Current, and Loan Accounts.

## Requirements

### 🏦 1. Base Class: Account

Attributes: account_number, account_holder, balance

Methods:

__init__() → initialize the account.

deposit(amount) → increases balance.

withdraw(amount) → decreases balance (check for sufficient funds).

display_info() → displays account details.

Use Encapsulation to make balance private and create getter and setter using property decorators.

### 💰 2. Derived Classes

SavingsAccount(Account)

Additional attribute: interest_rate

Method: add_interest() → adds interest to balance.

CurrentAccount(Account)

Additional attribute: overdraft_limit

Override withdraw() method → allows withdrawal up to overdraft limit.

LoanAccount(Account)

Additional attribute: loan_amount

Method: pay_emi(amount) → reduces loan amount.

These demonstrate Single and Multilevel Inheritance and Method Overriding.

### 👥 3. Multiple Inheritance Example

Create a class KYC (Know Your Customer) with:

Attributes: aadhaar_number, pan_number

Method: verify_kyc()

Now, create a class VerifiedSavingsAccount(SavingsAccount, KYC) that inherits from both and ensures account activation only after KYC verification.

### ⚙️ 4. Bank Utility Class

Create a class Bank with:

Class variable: bank_name = "PyBank"

Class method: get_bank_name()

Static method: bank_policy() → prints some static rules.

### 🔒 5. Abstraction

Create an abstract class Transaction with an abstract method execute_transaction().
Both DepositTransaction and WithdrawTransaction classes should inherit it and implement the logic.

### 🌀 6. Polymorphism

Write a function print_account_summary(account) that takes any account type (Savings, Current, Loan) and prints summary differently depending on the account type.

### ⚰️ 7. Destructor

When an account object is deleted, print a message like:

"Account [account_number] closed successfully."

### Expected Output Example

```python
Account Created: 1001 - Jaswanth
Deposit of ₹5000 successful
Withdrawal of ₹2000 successful
Interest added: ₹150
Balance after interest: ₹3150
Loan EMI of ₹1000 paid. Remaining Loan: ₹9000
KYC Verified: True
Account Summary for Savings Account of Jaswanth
Bank Policy: Maintain minimum ₹1000 balance
Account 1001 closed successfully.
```
