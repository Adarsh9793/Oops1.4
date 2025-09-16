class Employee:
    language = "Python" #This is a class attributes.
    company = "Google" #This is a class attributes.
    salary = 50000

    def __init__(self, name, salary,company,language):
        self.name = name #This is an instance attributes.
        self.salary = salary #This is an instance attributes.
        self.company = company #This is an instance attributes.
        self.language = language #This is an instance attributes.
        print("I am creating a object")
    
    
    @staticmethod
    def greet(self):
        print("Hello, welcome to the company!")
 
adarsh = Employee("Adarsh", 50000, "Google", "Python")
print(adarsh.name,adarsh.salary,adarsh.language,adarsh.company)

a = Employee(4)
a.greet()