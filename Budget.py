class Budget:



 my_budget = []
my_budget= Budget(food=1000, clothing=2000, rent=30000,entertainment=15000)
my_budget.deposit(2000,'food')
my_budget.withdraw(5000,'rent')
my_budget.transfer(700,'entertainment','clothing')
my_budget.check_balance('clothing')

def __init__(self,**categories):
        self.categories = categories
        print(self.categories)

def deposit(self,amount,category):
        self.categories[category] = self.categories[category] + amount
        print (f"You deposited the sum of $ {amount}+ " "+ to {category}")
    
def withdraw(self,amount,category):
        if amount >+ self.categories[category]:
            print("Amount not available")
        else:

            self.categories[category] = self.categories[category] - amount
            print (f"You withdrew the sum of $ {amount}+ " "+ {category}")

def transfer(self,amount,debit_category,credit_category):
        if amount > self.categories[debit_category]:
            print("Amount not available")
        else:
            self.categories[debit_category] = self.categories[debit_category] - amount
            self.categories[creditc_ategory] =  self.categories[credit_category] + amount
            print (f"You transfered the sum of $ {amount} + " " + 'from ' + {debit_category} + ' to '+ {credit_category}")
    
def check_balance(self,category):
        print("Your '+ category + ' budget balance is ' + str(self.categories[category])")
        

