class Employee():

    def __init__(self, name, surname, yearly_income):
        self.name = name
        self.surname = surname
        self.yearly_income = yearly_income
        

    def give_raise(self, amount=5000): # default = 5000
        self.yearly_income += amount

        