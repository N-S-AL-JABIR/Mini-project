from Food_menu import Food_menu
from Menu import Menu
from Restaurent import Restaurent
from Users import Customer, Admin, Employee, User
from Orders import Order

mama_res = Restaurent("mama res")


def customer_menu():
    name = input("Enter Your Name : ")
    email = input("Enter Your Email : ")
    phone = input("Enter Your phone : ")
    address = input("Enter Your address : ")
    customer = Customer(name, phone, email, address)

    while True:
        print(f"Welcome {customer.name}!")
        print(
            "1. View Menu\n"
            "2. Add Item to cart\n"
            "3. View cart\n"
            "4. Pay bill\n"
            "5. Exit"
        )
        choise = int(input("Enter your Choise : "))
        if choise == 1:
            customer.view_menu(mama_res)

        elif choise == 2:
            it_name = input("Enter Item Name: ")
            it_quentity = input("Enter Item quentity: ")
            customer.add_to_cart(mama_res, it_name, it_quentity)

        elif choise==3:
            customer.view_cart()

        elif choise==4:
            customer.pay_bill()

        elif choise==5:
            break
        else:
            print("Invalid Input")


def admin_menu():
    name = input("Enter Your Name : ")
    email = input("Enter Your Email : ")
    phone = input("Enter Your phone : ")
    address = input("Enter Your address : ")
    admin = Admin(name, phone, email, address)

    while True:
        print(f"Welcome {admin.name}!")
        print(
            "1. Add New Item\n"
            "2. Add New Employee\n"
            "3. View Employee\n"
            "4. View Items\n"
            "5. Delete Items\n"
            "6. Exit"
        )
        choise = int(input("Enter your Choise : "))

        if choise ==  1:
            it_name = input("Enter Item Name: ")
            it_ptice = input("Enter Item price: ")
            it_quentity = input("Enter Item quentity: ")
            item=Food_menu(it_name,it_ptice,it_quentity)
            admin.add_new_item(mama_res,item)

        elif choise == 2:
            name = input("Enter Employee Name : ")
            email = input("Enter Employee Email : ")
            phone = input("Enter Employee phone : ")
            address = input("Enter Employee address : ")
            desig = input("Enter Employee designation : ")
            salary = input("Enter Employee salary : ")
            age = input("Enter Employee age : ")
            employee = Employee(name,phone,email,address,age,desig,salary)
            admin.add_employee(mama_res,employee)

        elif choise == 3:
            admin.view_employee(mama_res)

        elif choise == 4:
            admin.view_menu(mama_res)
        elif choise == 5:
            item_name= input("Enter item Name: ")
            admin.remove_item(mama_res,item_name)
        elif choise==6:
            break
        else:
            print("Invalid Input")


while True:
    print(f"Welcome!")
    print(
        "1. Customer\n"
        "2. Admin\n"
        "3. Exit"
    )
    choise = int(input("Enter your Choise : "))
    if choise == 1:
        customer_menu()

    elif choise == 2:
        admin_menu()
    elif choise == 3:
        break
