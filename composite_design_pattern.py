#The Composite Design Pattern is a structural design pattern that lets you compose objects into tree structures to represent part-whole hierarchies. 
#This pattern allows clients to treat individual objects and compositions of objects uniformly.


from abc import abstractstaticmethod, abstractmethod, ABC


class Department(ABC):  #component class: abstract class or interface that declares the common interface for all concrete classes or childclasses 

    @abstractmethod
    def __init__(self, employees):
        #implementation in child class
        pass
    @abstractstaticmethod
    def print_department():
        #implementation in child class
        pass

class HRDepartment(Department):   #leaf class: concrete class that implements the Component interface. It represents the individual objects in the composition. Leafs have no children.

    def __init__(self, employees):
        self.employees = employees

    def print_department(self):
        print(f"HR Department has {self.employees}")

class SalesDepartment(Department):

    def __init__(self, employees):
        self.employees = employees

    def print_department(self):
        print(f"Sales Department has {self.employees}")

class ParentDepartment(Department):   #composite class: This is a concrete class that implements the Component interface as well. However, a composite can have child components, which can be either leaf nodes or other composites. The composite class delegates operations to its children.

    def __init__(self, employees):
        self.employees = employees
        self.base_employees = employees
        self.sub_depts = []

    def add_sub_department(self, sub_dept):
        self.sub_depts.append(sub_dept)
        self.employees += sub_dept.employees

    def print_department(self):
        print("This is parent department")
        print(f"Parent depratment has {self.base_employees} base employees")
        for dept in self.sub_depts:
            dept.print_department()
        print(f"Total number of employees: {self.employees}")



hr_dept = HRDepartment(10)
sales_dept = SalesDepartment(50)
parent_dept = ParentDepartment(15)
parent_dept.add_sub_department(hr_dept)
parent_dept.add_sub_department(sales_dept)

parent_dept.print_department()

