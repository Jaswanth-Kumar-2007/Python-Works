class BankAccount:
    def __init__(self,owner,_balance):
        self.owner = owner
        self._balance = _balance

    def deposit(self,amount):
        self._balance += amount
        return self._balance
        
    def withdraw(self,amount):
        if amount > self._balance:
            return "Insufficient funds"
        else:
            self._balance -= amount
            return self._balance

    def display_balance(self):
        return f"Balance : {self._balance}"

acc = BankAccount("Alice", 1000)
print(acc.deposit(500))
print(acc.withdraw(2000))
print(acc.display_balance())
print(acc.withdraw(100))
print(acc.display_balance())
