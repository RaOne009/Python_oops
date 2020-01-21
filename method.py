class Employee:
    increase = 1.5
    def __init__(self,fname, lname, income):
        self.fname = fname
        self.lname = lname
        self.income = income
#todo nothing use pass (kush ni)
    pass

    def increase(self):
        self.income = self.income * self.increase

    @classmethod
    def change_incremeent(cls, amount):
        cls.Employee = amount
        pass

tony = Employee('Tony', 'stark', 400000)
rohit = Employee('Rohit', 'sharma', 500000)
Employee.change_incremeent(2)
tony.increase()
print(tony.income)
# print(tony.__dict__)
# tony.increase()
