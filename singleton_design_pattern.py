#Tutorials from https://youtube.com/playlist?list=PL7yh-TELLS1FuqLSjl5bgiQIEH25VEmIc&feature=shared


#The Singleton design pattern is a creational design pattern that ensures a class has only one instance and provides a global point of access to that instance. 



from abc import ABCMeta, abstractstaticmethod



# The @abstractstaticmethod decorator is used to declare the print_data method as an abstract static method, indicating that it must be implemented by subclasses.


class Person(metaclass=ABCMeta):     #The Person class is defined with ABCMeta as its metaclass. 
    
    @abstractstaticmethod  ## The @abstractstaticmethod decorator is used to declare the print_data method as an abstract static method, indicating that it must be implemented by subclasses.   
    def print_data():     ##This means that Person is an abstract base class, and any class inheriting from it must implement the abstract method print_data. 
        pass


class PersonSingleton(Person):

    __instance = None        #The __instance variable is used to store the instance of the Person class. basically an instance tracker

    @staticmethod
    def get_instance(): #new instance of PersonSingleton with default values or returns the existing instance if it has already been created.
        if PersonSingleton.__instance == None: 
            PersonSingleton("Default Name", 0)  #If instance has not been created yet then this default instance is created with the name set to "Default Name" and age set to 0.
        return PersonSingleton.__instance
    
    def __init__(self, name, age):   
        if PersonSingleton.__instance != None:
            raise Exception("This class is a singleton!") #It checks if an instance already exists and raises an exception if an attempt is made to create another instance.
        else:                                        #If not, it sets the instance and initializes the name and age attributes.
            PersonSingleton.__instance = self
            self.name = name
            self.age = age

    @staticmethod
    def print_data():
        print(f'Name: {PersonSingleton.__instance.name}, Age: {PersonSingleton.__instance.age}') 

    