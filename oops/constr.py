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



s1 = Student({"name" :"Rahul", "rollNumber": "0001", "age": 20})
# print(s1.getInfo()["age"])
print(s1._Student__name)



