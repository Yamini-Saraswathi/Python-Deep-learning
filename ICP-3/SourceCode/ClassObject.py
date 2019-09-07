class Employee:
    EmployeeCount = 0
    SalarySum = 0
    def __init__(self,name, family, salary, department):
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department
        Employee.SalarySum += self.salary
        Employee.EmployeeCount += 1
    def AverageSalary(self):
        print("Average Salary of Employees", Employee.SalarySum/Employee.EmployeeCount)
class FullTimeEmployee:
    def __init__(self, name, family, salary, department):
        Employee.__init__(self, name, family, salary, department)

e1 = Employee("yamni","bommineni", 100, "a")
e2 = Employee("Khalida", "Shaik", 200, "b")
e3 = Employee("Swara","Thota", 300, "c")

print("Sum of Salaries of Employees :", Employee.SalarySum)
print("Number of Employees :", Employee.EmployeeCount)
Employee.AverageSalary(e1)
