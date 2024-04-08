# 1. Encapsulation in Personal Budget Management

# Task 1: Define Budget Category Class
class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget
        self.expenses = 0
    
    def get_my_category(self):
        return self.__category_name
    
    def get_my_budget(self):
        return self.__allocated_budget
    
    def set_category(self, new_category):
        self.__category_name = new_category

    def set_budget(self, new_budget):
        self.__allocated_budget = new_budget
    
    def add_expenses(self, amount):
        if 0 < amount <= self.__allocated_budget:
            self.set_budget(self.get_my_budget() - amount)
            self.expenses += amount
        else:
            print(f'You are outside of your budget.')
    
    def display_category_summary(self):
       print(f'You have {self.__allocated_budget} left of your {self.__allocated_budget + self.expenses} budget for {self.__category_name}.')
    
my_budget = BudgetCategory('Food', 200)

my_budget.add_expenses(100)

print(f'I am allowed to spend {my_budget.get_my_budget()}, on {my_budget.get_my_category()}')
my_budget.display_category_summary()
