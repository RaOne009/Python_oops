#1st class
class Employee:
    #constructer
    def __init__(self, fname, lname, income):
        self.fname = fname
        self.lname = lname
        self.income = income
#todo nothing use pass (kush ni)
    pass
tony = Employee("tony", "stark", "40000")
rohit = Employee("rohit", "sharma", "50000")

# tony.fname = "tony"
# tony.lname = "stark"
# tony.income = "40000"
#
# rohit.fname = "rohit"
# rohit.lname = "sharma"
# rohit.income = "40000"
#
 print(tony.income)
 print(rohit.fname, tony.lname)
