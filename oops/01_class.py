class employee:
    name = "John"
    age = 30
    salary = 50000

    def getInfo(self):
        print(f'Name: {self.name}, Age: {self.age}, Salary: {self.salary}')

    @staticmethod
    def getDate():
        print("Date of Joining: 2020-01-01")
        


emp1 = employee()
# emp1.getInfo()
emp1.getDate()

