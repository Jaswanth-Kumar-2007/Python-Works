class Account:
    ac_no = 1000

    def __init__(self,account_holder,balance = 0):
        self.account_holder = account_holder

        self.__balance = balance

        self.account_number = ac_no + 1

        print(f"Account Created {self.account_number}-{self.account_holder}")
 
    def deposit(self,amount):
        self.__balance += amount
        print("Money Deposited Successfully")

    def withdraw(self,amount):
        if amount > self.amount:
            print("Insufficient Balance")
        else:
            self.__balance -= amount
            print("Money Withdraw Successfully")

    def display_info(self):
        print(f"Account Holder : {self.account_holder}")
        print(f"Account No. : {self.account_number}")
        print(f"Current Balance : {self.__balance}")

class Savings(Account):
    def __init__(self,account_holder,balance=0,interest_rate=0.05):
        super.__init__(account_holder,balance)
        self.interest_rate = interest_rate

    def interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)
        print(f"Interest Added {interest}")

class LoanAccount(Account):
    def __init__(self,account_holder,balance = 0,loanamount = 0):
        super.__init__(account_holder,balance)
        self.loanamount = loanamount

    def loan(self,amount):
        if self.balance != 0:
            self.loanamount += amount
            print("Loan Sanctioned Successfully")
        else:
            print("Account Balance Need Not Be Zero")

    def pay_emi(self,amount):
        if amount > self.loanamount:
            print("loanamount = 0")
