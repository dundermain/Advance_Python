#Tutorials from https://youtube.com/playlist?list=PL7yh-TELLS1FuqLSjl5bgiQIEH25VEmIc&feature=shared

#abstract class is a class that has atleat one abstract method and by abstarct method we mean that it can only be used by subclasses.
#abstract class cannot be instantiated on thier own or objects cannot be formed from absrtract classes.
#abstract class is needed when we want to our subclasses to have some common methds yet different implementation
#abstarct methods are methods that have definition but we cannot implement it. These methods needs to be implemented by the subclasses
#in nutshell, abstarct class provide blueprint for other classes

#an example is given below

from abc import ABC, abstractmethod
 
class Polygon(ABC):
 
    @abstractmethod
    def noofsides(self):                                  #abstract method that must be implemented by the subclasses
        pass
 
 
class Triangle(Polygon):
 
    # overriding abstract method
    def noofsides(self):
        print("I have 3 sides")
 
 
class Pentagon(Polygon):
 
    # overriding abstract method
    def noofsides(self):
        print("I have 5 sides")
 
# Driver code
R = Triangle().noofsides()
R = Pentagon().noofsides()
 

#Now imagine we donot want to creat an object and we let users to create object, then factory design setup comes in which will dynamically create an object of the required class
#here is an example


from abc import ABC, abstractmethod
 
class Polygon(ABC):
 
    @abstractmethod
    def noofsides(self):                                  #abstract method that must be implemented by the subclasses
        pass
 
 
class Triangle(Polygon):
    def noofsides(self):
        print("I have 3 sides")
 
 
class Pentagon(Polygon):
    def noofsides(self):
        print("I have 5 sides")


class sides:

    @staticmethod
    def choose_sides(sides):
        if sides == 3:
            Triangle().noofsides()

        elif sides == 5:
            Pentagon().noofsides()
        
        else:
            print("Invalid number of sides")


sides.choose_sides(3)