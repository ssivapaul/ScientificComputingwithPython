import math

class Category:   
    def __init__(self, name):
        self.balance = 0
        self.name = name
        self.ledger = []
        
    def __str__(self):
        result = ''
        result=self.name.center(30,'*') + '\n'
        for element in self.ledger:
            result += element['description'][:23].ljust(23) + str(f"{element['amount']:<5.2f}").rjust(7) + '\n'
        result += 'Total: ' + str(round(self.balance, 2))
        return result
    # f"{number:<10.2f}"    
    # A deposit method that accepts an amount and description. 
    # If no description is given, it should default to an empty string. 
    # The method should append an object to the ledger list in the form of 
    # {'amount': amount, 'description': description}
    
    def deposit(self, amount, description = ''): 
        self.balance += amount
        self.ledger.append({'amount': amount, 'description': description})

    # A withdraw method that is similar to the deposit method, 
    # but the amount passed in should be stored in the ledger as a negative number. 
    # If there are not enough funds, nothing should be added to the ledger. 
    # This method should return True if the withdrawal took place, and False otherwise.

    def withdraw(self, amount, description = ''):
        if self.check_funds(amount):
            self.balance -= amount
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False       

    # A get_balance method that returns the current balance of 
    # the budget category based on the deposits and 
    # withdrawals that have occurred.
    
    def get_balance(self):
        return self.balance

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
    
# Besides the Category class, create a function (outside of the class) called 
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
    chart = ''
    
    e = [[-ledger['amount'] for ledger in cat.ledger if ledger['amount'] < 0] for cat in categories] 
    expense = [sum(i) for i in e]
    total = sum(expense) # Expense list
    print()
    print(expense)
    print("Total: ", total)
    percent = list(map(lambda x: int(x/total*100/10)*10 , expense)) # Expense list round to 10
    #percent = list(map(lambda x: math.floor(x/total*100/10)*10 , expense))
    print(percent)
    per = [('o'*(i//10 + 1)).rjust(11) for i in percent] # padded expense bar
    print(per)
    bar = [ ''.join([p[i] + ' '*2 for p in per]) for i in range(11)] #  
    #print(bar)
    category_name_list = [(n.name) for n in categories] # create category name portion of string  
    max_name_length = len(max(category_name_list, key=len))
    padded_name_list = [name.ljust(max_name_length) for name in category_name_list]
    
    chart += 'Percentage spent by category' + '\n' 
    chart += ''.join([str(i).rjust(3)+'| ' + bar[(100-i)//10] + '\n' for i in range(100, -10, -10)])
    chart += ' '*4 + '-' + '---'*len(categories) + '\n'
    chart += ''.join([(' '*5 + ''.join(n[i] + '  ' for n in padded_name_list) + '\n') if i < max_name_length -1 else (' '*5 + ''.join(n[i] + '  ' for n in padded_name_list)) for i in range(max_name_length)])
    
    print('\n')
    return chart

food = Category('Food')
food.deposit(1900, 'deposit')
food.withdraw(11, 'milk, cereal, eggs, bacon, bread')
clothing = Category('Clothing')
food.transfer(500, clothing)
clothing.withdraw(50.75, 'Shirt, trousers')
auto = Category('Car')
auto.deposit(200, 'deposit')
auto.withdraw(75.345, 'tires, service')
cat = [food, clothing, auto]
print(food)
print(clothing)
print(auto)
print(create_spend_chart(cat))
