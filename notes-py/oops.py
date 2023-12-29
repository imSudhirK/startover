# CLASS 
# user define data structure 
# blueprint or protoype of object

# CLASS OBJECTS
# instance of class with actual values

# python has garbage collector
# which handles memory management itself


# ENCAPSULAION
# similar to api
# varibles are wrapped in functions 
# call corresponding function to access 


# Public variables 
# accessed and modified anywhere 
# publicVar = 123

# Protected variables
# accessed in class as well as subclass 
# _protecttedVar = 123

# Private variables 
# accssed only within class
# __privateVar = 123

# in python public and private is myth



# FUNCTION OVERLOADING 
# assignment of more than one behaviour 
# to a particular function

# INHERITANCE
# transfer of characteristic of a class
# to other classes that are derived from it


# class ClassName:
#    'Optional class documentation string'
#    class_suite

# ClassName.__doc__


class Employee:
    '''this is employee class documentation
    this is second line of documentation'''
    employee_count =0       #shared among all the instances of a in this class

    # constructor
    def __init__ (self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_count +=1

    #  class method
    def displayCount(self):
        print("total Employees: %d" % Employee.employee_count)
    
    # don't need to pass self argument while calling
    def displayEmployee(self):
        print("Name: ", self.name, ", Salary: ", self.salary)
    
    # distructor
    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "distroyed")

print("Documentation: Employee.__doc__ \n", Employee.__doc__)
print("Dictionary: Employee.__dict__\n", Employee.__dict__)
print(Employee.__name__)

# instance object
# call the class with class name
# and pass the arguments whatever __init__ accepts
emp0 = Employee("zara", 20000)

emp0.displayEmployee()
emp0.displayCount()

print(hasattr(emp0, 'salary'))
print(getattr(emp0, 'salary'))
delattr(emp0, 'salary'); print(hasattr(emp0, 'salary'))
setattr(emp0, 'salary', 60000); print(getattr(emp0, 'salary'))

# CLASS INHERITANCE 
class ParentClass:
    parentAttr = 100

    def __init__ (self):
        print("called parent constructor")
    def setAttr(self, attr):
        self.parentAttr = attr
    def getAttr(self, attr):
        return self.parentAttr
    def myMethod(self):
        print("calling parents method")


class ChildClass(ParentClass):
    childAttr = 50
    
    def __init_(self):
        print("called Child Class")
    def myMethod(self):
        print("calling child method")
    

child = ChildClass()
print(child.parentAttr)
child.setAttr(200); print(child.parentAttr)
print(child.getAttr("parentAttr"))
child.myMethod() # childs method override
print("issubclass (child, parent ): ", issubclass(ChildClass, ParentClass))
print("isinstance(child, ChildClass): ",isinstance(child, ChildClass))
# class A:        # define your class A
# class B:         # define your calss B
# class C(A, B):   # subclass of A and B

# Protected Data
# name attribute with double underscore prefix
class JustCounter:
    __secretCount = 100
    def getCount(self):
        return self.__secretCount
    
jcobj = JustCounter()
print(jcobj.getCount())
# print(jcobj.__secrectCount)
print(jcobj._JustCounter__secretCount)