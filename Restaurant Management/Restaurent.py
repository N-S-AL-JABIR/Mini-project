from Menu import Menu
class Restaurent:
    def __init__(self, name):
        self.name = name
        self.employees = []
        self.menu = Menu()

    def add_employee(self, employee):
        self.employees.append(employee)

    def view_employee(self):
        print("employee list")
        for emp in self.employees:
            print(emp.email, emp.phone, emp.name)
