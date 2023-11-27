# proxy design pattern are kind of decorator where object is created therough a proxy class which inturn is connected to main class

#lets see an example

from abc import ABC, abstractmethod

class Polygon(ABC):
    @abstractmethod
    def noofsides(self):
        pass

class Triangle(Polygon):
    def noofsides(self):
        print("I have 3 sides")

class ProxyPolygon(Polygon):             #here we created a proxy class that is a subclass of main polygon class

    def __init__(self):
        self.triangle = Triangle()      #now here instead of instantiating directly, we instantiated the triangle class through proxy class

    def noofsides(self):
        return self.triangle.noofsides()
    

ProxyPolygon().noofsides()   #now here we will not know that the proxy class 