#OOPS concept in Python
#https://www.youtube.com/watch?v=-pEs-Bss8Wc

class SoftwareEngineer:
    #created a clase

    alias = "Keyboard Magician"  #  This is a class attritbute. It can be accessed by both class and instance

    def __init__(self, name, age, level, salary):  #for every method in an instanse the first argument has to be self. This is initialisation
        self.name =  name
        self.age = age
        self.level = level 
        self.salary = salary   #all these are instance attributes and can only be accssed by instance not by class

    def code(self): #This is an instance method. A method is a function inside thre class and attribute is variable inside class
        print(f"{self.name} is writing a code")

    def code_in_language(self, langauge): #we can pass arguments in methods as well
        print(f"{self.name} is writing a code in {langauge}")


#some dunder methods available in Python. dunder means double under methods

    def __str__(self):   #__str__ returns human readable string represenation of an object/instance 
        information = f"The name of the SE is {self.name}, age is {self.age}. {self.name} is working at level {self.level}"
        return information
    
    def _eq__(self, other): #__eq__ returns boolean as per our choice. UNlike ==, which compares object only, __eq__ can be used to compare attributes
        return self.name == other.name and self.age == other.age
    
    #Now if we want a clas method that can work for instance/object as well
    #we use static method decorator

    @staticmethod  #static method can be used even without calling object. If we dont use static method, then the method can only be accessed by class and not by object/instance
    def entry_salary(age):  #we cannot use self attribute here as static methods can be accesses without object/instance
        if age<25:
            return 5000
        if age<30:
            return 7000
        return 9000

    



se1 = SoftwareEngineer("Max", 20, "Junior", 5000)  #created an instance with their respecitve attributes as arguments



print(se1.age)
print(se1.alias)
print(SoftwareEngineer.alias)
se1.code()
#print(SoftwareEngineer.age)  #this will give error "AttributeError: type object 'SoftwareEngineer' has no attribute 'age'"

print(se1) #This will call the __str__method and will print the information present there

#Lets create another object with identical attributes as se1
se2 = SoftwareEngineer("Max", 20, "Junior", 5000)

print(se1 == se2) #This shpuld return True but it returns false because it compares the memory location. Since memory location will always be different 
#hence it return false altough the object are identical to each other. Therefore we use __eq__ for comparison of objects attributes. Equality operator will
#only check the object. If the object is same it will return true otherwise false. It doesnot care about whether the objects attributes are same or not

print(SoftwareEngineer.entry_salary(27))