class Employees: # Create base Class Employees
    def __init__(self, employeeNo, employeeName): #Create objects self, employeeNo, and EmployeeName
        self.employeeNo = employeeNo #Create attribute employeeNo
        self.employeeName = employeeName
        self.employeeSalary = None
    def calculateSalary(self):
        raise NotImplementedError("Subclass has to implement method")
class Hourly(Employees):
    def __init__(self, employeeNo, employeeName):
        Employees.__init__(self, employeeNo, employeeName)
        self.hoursWork = None
        self.ratePay = None
    def calculateSalary(self):
        self.hoursWork = input("How many hours did you work in a week?")
        self.ratePay = input("Rate of pay:")
        self.employeeSalary = int(self.hoursWork)*float(self.ratePay)*52
class YearlySupervisor(Employees):
    def __init__(self, employeeNo, employeeName):
        Employees.__init__(self, employeeNo, employeeName)
        self.year = None
        self.baseRate = None
    def calculateSalary(self):
        self.year = int (input("How many years have you worked for the company?"))
        self.baseRate = input("Base pay is:")
        if self.year <=5:
           self.employeeSalary = int(self.baseRate)
        else:
           self.employeeSalary = int(self.baseRate)*1.5
employee = list()
employee.append(Hourly(1111,"Alice"))
employee.append(YearlySupervisor(2222, "Betty"))
for empl in employee:
    empl.calculateSalary()
    print(empl.employeeName," has a salary of",empl.employeeSalary,"per year.")
