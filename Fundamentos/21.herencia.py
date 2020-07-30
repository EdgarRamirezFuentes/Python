class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    ## Getters
    def getName(self):
        return self.__name
    
    def getAge(self):
        return self.__age
    
    ## Setters
    def setName(self, name):
        self.__name = name
        
    def setAge (self, age):
        self.__age = age
        
    def __str__(self):
        return "Name: " + self.__name + " Age: " + str(self.__age)

class Employee(Person): ## Entre paréntesis se indica la clase de la que hereda.
    def __init__(self, name, age, salary):
        super().__init__(name, age) ## Inicializa los valores de la clase padre
        self.__salary = salary
    
    ## Getters 
    
    def getName(self):
        return super().getName()
    
    def getAge(self):
        return super().getAge()
    
    ## Setters
    
    def setName(self, name):
        super().setName(name)
    
    def setAge(self, age):
        super().setAge(age)

    def setSalary(self, salary):
        self.__salary = salary
        
    def __str__(self):
        return super().__str__() + " Salary: " + str(self.__salary)
    
    

employee = Employee("Edgar Ramírez Fuentes", 21, 20500.00)
employee.setName("Edgar Alejandro Ramírez Fuentes")
print(employee.__str__())    
        
    
        