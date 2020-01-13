#1st class
class Employee:
    #constructer
    def __init__(self, fname, lname, income):
        self.fname = fname
        self.lname = lname
        self.income = income
#todo nothing use pass (kush ni)
    pass
tony = Employee('Tony', 'stark', 400000)
rohit = Employee('Rohit', 'sharma', 500000)

# tony.fname = "tony"
# tony.lname = "stark"
# tony.income = "40000"
#
# rohit.fname = "rohit"
# rohit.lname = "sharma"
# rohit.income = "40000"

 print(tony.income)
 print(rohit.fname, tony.lname)
