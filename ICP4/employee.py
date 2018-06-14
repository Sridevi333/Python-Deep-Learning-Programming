# Create a class Employee and then do the followinga.
# Create a data member to count the number of Employeesb.
# Create a constructor to initialize name, family, salary, department
#  Create a function to average salary.
# Create a Fulltime Employeeclass and it should inherit the properties of Employee classe.
# Create the instances of Fulltime Employeeclass and Employee class and call their member functions.
class Employee():
    'Common base class for all employees'
    empCount = 0
    SumSalary =0
    Avg =0

    def _init_(self, eid, name, salary, did):
        self.eid = eid
        self.name = name
        self.salary = salary
        self.did = did
        Employee.empCount += 1
        Employee.SumSalary += self.salary

    def displayEmployee(self):
        print("eid : ", self.eid, ", Name : ", self.name, ", Salary: ", self.salary, ", did: ", self.did)

class FullTimeEmp(Employee):
    def _init_(self, eid, name, salary, did, exp):
        Employee._init_(self, eid, name, salary, did)
        self.exp = exp
    def displayEmployee(self):
        print("eid : ", self.eid, ", Name : ", self.name, ", Salary: ", self.salary, ", did: ", self.did, ",Experience:", self.exp)


"This would create first object of Employee class"
emp1 = Employee(1, "Sri", 2000, 10)
"This would create second object of Employee class"
emp2 = Employee(2, "Devi", 4000, 20)
emp3=FullTimeEmp(3, "Mallipudi", 4000, 20, 6)
emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employees %d" % Employee.empCount)
print("Average salary of the employees is", (Employee.SumSalary/Employee.empCount))
print(emp1.displayEmployee())
print(emp2.displayEmployee())
print(emp3.displayEmployee())