# Q)  Employee Salary Management system 
# Question --->
""" 
Create a class Employee with:
Private attributes: __name, __salary
Public method to give a raise, update name, and display data.
Ensure salary cannot be negative using property methods.
"""
# Answer --> 

class Employee:
    def __init__(self, name, salary):
        # Wrong type input Error Handaling
        if not isinstance(salary, (int,float)):
            raise TypeError("Salary Should be in Number")
        
        # Negative input Error handaling   
        if salary <= 0:
            raise ValueError(" Negative Salary Not Allowed...!")
        else:
            self.__name = name
            self.__salary = salary
            self.percentage = 0
            self.Amount_increased = 0
    def Increase(self, percentage):
        self.percentage = percentage
        self.Amount_increased = (percentage/100) * self.__salary
        self.__salary += self.Amount_increased
    
    def UpdateName(self, U_name):
        self.__name  = U_name
        
    def GetData(self):
        print(f"|E Name:{self.__name:>22}|\n"
              f"|Salary Before: {self.__salary - self.Amount_increased:>13.2f}\u20B9|\n"
              f"|Percentage: {self.percentage:>16}%|\n"
              f"|Amount Increased: {self.Amount_increased:>10.2f}\u20B9|\n"
              f"{'-'*30}\n"
              f"|Salary After: {self.__salary:>14.2f}\u20B9|")
        

try:       
    e1 = Employee("Abhi", 55000)
    print("-"* 30)
    e1.Increase(30)
    e1.UpdateName("Abhishek K")
    e1.GetData()
    print("-"* 30)

except ValueError as salary_wrong:
    print(salary_wrong)

except TypeError as wrong_type:
    print(wrong_type)
