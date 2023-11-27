# OOPS Inheritance concepts
#https://www.youtube.com/watch?v=-pEs-Bss8Wc

#Inheritance is a method where one class(child class) uses attritbues and methods of another class(Parent Class). 

class Employee:   #parent class. Child can inherit

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def work(self):  #This is parent or base method since it is present in parent class
        print(f"{self.name} is working.")
    

class SoftwareEngineer(Employee):  #child class. It will use some attributes of Employee parent class

    def __init__(self, name, age, salary, level):
        super().__init__(name, age, salary)     #we dont need to call self.name again here as it is present in our parent class. super() means super class or parent class. This will override the parent class attributes
        self.level = level    #extending the attributes

    def debug(self):
        print(f"{self.name} is debugging")

    def work(self):  #When we use the base method inside the instance, it will override the parent/base method
        print(f"{self.name} is coding.")

class Designer(Employee):

    def draw(self):
        print(f"{self.name} is drawing")

se = SoftwareEngineer("Max", 25, 7000, "Junior")
se.work()   #example of inheritance where the child class overrides the parent class methods
se.debug()  #example of extend where we extended the child class by adding a new method

d = Designer("Philip", 27, 7000)
d.work()  #example of inheritance where the child class inherited the parent class methods
d.draw()
print(d.name) 


#Polymorphism 
#It gives a way to use a parent class method where the child class can still keep its own methods as they are
#

employees = [SoftwareEngineer("Max", 25, 6000, "Junior"), 
             SoftwareEngineer("Lisa", 30, 9000, "Senior"),
             Designer("Philips", 27, 7000)]


def motivate_employees(employees):
    for employee in employees:
        employee.work()


motivate_employees(employees)