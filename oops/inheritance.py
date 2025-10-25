from datetime import date

class Student:   
    def __init__(self, info): # Dander Method which is called automatically when object is created
        self.setInfo(info["name"], info["rollNumber"], info["age"])

    def setInfo(self, name, rollNumber, age):
        self.__name = name
        self.__rollNumber = rollNumber
        self.__age = age

    def getInfo(self):
        return {"name": self.__name, "roll": self.__rollNumber, "age": self.__age}

    def great(self):
        print(f'Hello {self.__name}')

    @staticmethod
    def today():
        print(f"Today is a {date.today().strftime('%A')} and date is {date.today().strftime('%d-%m-%Y')}")



class Employee(Student):
    company = "Microsoft"

    def great(self):
        super({"name": "Employee"})
        print(f'Welcome to the company {self.company}')



s1 = Employee()
print(s1.great())



