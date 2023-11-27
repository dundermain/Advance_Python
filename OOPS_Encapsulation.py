#Here we will discuss about encapsulation and abstarction
#https://www.youtube.com/watch?v=-pEs-Bss8Wc

#Encapsulation is a mechanism of hiding of data implementation. Instance attributes/methods can be hidden or made private. 
#This can only be accessed by accessor like getter setter method

class SoftwareEngineer:

    def __init__(self, name, age):
        self.name = name
        self.age =  age

        #Lets salary and number of bugs solved attribute to private
        # One underscore (e.g _x) is called "protected attribute or method"
        # double underscore (e.g. __x) is called "private attribute or method"
        self._salary =  None
        self._num_bugs_solved = 0
        
    #now lets assume someone wants to access the private attributes
    #We will use getter setter method

    def get_salary(self):
        return self._salary
    
    def set_salary(self, value):
        self._salary = value


    #Now let us assume we want to calculate salary on the basis of number of bugs resolved
    #We can create a private method to do this becuase we donot want to expose the salary details and number of bugs solved

    #lets define a function that will count number of bugs resolved by an engineer
    def code(self):
        self._num_bugs_solved += 1

    def get_salary(self):
        return self._salary
    
    def set_salary(self, base_value):
        self._salary = self._calculate_salary(base_value)

    def _calculate_salary(self, base_value):
        if self._num_bugs_solved < 10:
            return base_value
        if self._num_bugs_solved <100:
            return base_value*2
        return base_value*3

    #There is more neat way to write getter and setter propeties and that is through decorators
    #Lets write the above getter setter code using decorators

    @property #decorator
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, value):
        self._salary = value

    #now if we want to delete the salary
    @salary.deleter
    def salary(self):
        del self._salary




se = SoftwareEngineer("Max", 25)
print(se.age, se.name)

#This calculates the number of bugs resolved
for i in range(300):
    se.code()


se.set_salary(6000)
print(se.get_salary())

#Using decorator method to get the salary
se.salary = 6000
print(se.salary)
