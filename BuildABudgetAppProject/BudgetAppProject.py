class Category:   
    def __init__(self, name):
        self.balance = 0
        self.name = name
        self.ledger = []
        
    def __str__(self):
        result = ''
        title = self.name.center(30, '*') + '\n'
        item_list = ''
        total = 0
        for dsc_amt in self.ledger:
            item_list += dsc_amt['description'][:23].ljust(23) + str(dsc_amt['amount'])[:7].rjust(7) +'\n'
            total += dsc_amt['amount']
        total = 'Total: ' + str(total)
        result = title + item_list + total    
        return result

    # A deposit method that accepts an amount and description. 
    # If no description is given, it should default to an empty string. 
    # The method should append an object to the ledger list in the form of 
    # {'amount': amount, 'description': description}
    
    def deposit(self, amount, description = ''): 
        self.balance += amount
        self.ledger.append({'description': description, 'amount': amount})

    # A withdraw method that is similar to the deposit method, 
    # but the amount passed in should be stored in the ledger as a negative number. 
    # If there are not enough funds, nothing should be added to the ledger. 
    # This method should return True if the withdrawal took place, and False otherwise.
    
    def withdraw(self, amount, description = ''):
        if self.check_funds(amount):
            self.balance -= amount
            self.ledger.append({'description': description, 'amount': -amount})
            return True
        else:
            return False       

    # A get_balance method that returns the current balance of 
    # the budget category based on the deposits and 
    # withdrawals that have occurred.
    
    def get_balance(self):
        return f'{self.balance}'

    # A transfer method that accepts an amount and another budget category as arguments. 
    # The method should add a withdrawal with the amount and the description 
    # 'Transfer to [Destination Budget Category]'. 
    # The method should then add a deposit to the other budget category with 
    # the amount and the description 'Transfer from [Source Budget Category]'. 
    # If there are not enough funds, nothing should be added to either ledgers. 
    # This method should return True if the transfer took place, and False otherwise.

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.name}')
            category.deposit(amount, f'Transfer from {self.name}')
            return True
        else:
            return self.withdraw(amount, f'Transfer to {category.name}')

    # A check_funds method that accepts an amount as an argument. 
    # It returns False if the amount is greater than the balance of the budget category and 
    # returns True otherwise. This method should be used by both the 
    # withdraw method and transfer method.

    def check_funds(self, amount):
        return self.balance >= amount
       
    # create_spend_chart that takes a list of categories as an argument. 
    # It should return a string that is a bar chart.

    # The chart should show the percentage spent in each category passed in to the function. 
    # The percentage spent should be calculated only with withdrawals and not with deposits. 
    # Down the left side of the chart should be labels 0 - 100. 
    # The 'bars' in the bar chart should be made out of the 'o' character. 
    # The height of each bar should be rounded down to the nearest 10. 
    # The horizontal line below the bars should go two spaces past the final bar. 
    # Each category name should be written vertically below the bar. 
    # There should be a title at the top that says 'Percentage spent by category'.

    def create_spend_chart(categories):
        pass

