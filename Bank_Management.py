import random


class Bank:
    _bank_balance = 0
    user_list = []
    admin_list = []
    total_loan = 0
    is_loan = True
    bankrupt = False

    def entry_user(self, user):
        self.user_list.append(user)

    def entry_admin(self, adm):
        self.admin_list.append(adm)

    def add_money(self, amount):
        Bank._bank_balance += amount

    def add_loan(self, amount):
        Bank.total_loan += amount

    def withdraw_f_bank(self, amount):
        Bank._bank_balance -= amount

    @classmethod
    def find_user_by_ac_no(cl, ac_no):
        for user in cl.user_list:
            if user.ac_no == ac_no:
                return user
        return None

    def delete_user_by_ac_no(cl, ac_no):
        for user in cl.user_list:
            if user.ac_no == ac_no:
                cl.user_list.remove(user)
                print(f"User with account number {ac_no} has been deleted.")
                return
        print(f"User with account number {ac_no} not found.")

    @classmethod
    def find_admin(cl, em):
        for ad in cl.admin_list:
            if ad.email == em:
                return ad
        return None

    @classmethod
    def check_main_balance(cl):
        print(f"Total available balance in the bank: {cl._bank_balance} tk")

    @classmethod
    def check_loan(cl):
        print(f"Total loan amount in the bank: {cl.total_loan} tk")

    @classmethod
    def toggle_loan_feature(cl):
        cl.is_loan = not cl.is_loan
        status = "enabled" if cl.is_loan else "disabled"
        print(f"Loan feature is now {status}")


class User(Bank):
    def __init__(self, name, email, passward, address, ac_type):
        super().entry_user(self)
        self.name = name
        self.email = email
        self.address = address
        self.ac_type = ac_type
        self.passward = passward
        self.balance = 0
        self.ac_no = random.randint(1000000000, 2000000000)
        self.transaction = []
        self.loan_count = 0
        self.loan_take = 0

    def deposite(self, amount):
        self.balance += amount
        self.add_money(amount)
        self.transaction.append({"Cash in": amount})
        print("Deposite Successfull")

    def withdraw(self, amount):
        if self.bankrupt == False:
            if self.ac_type.upper() == "SAVINGS":
                print(
                    "You can't withdraw your money, your account is a Savings account."
                )
                return

            if self.balance >= amount:
                self.balance -= amount
                self.withdraw_f_bank(amount)
                self.transaction.append({"Cash out": amount})
                print("Withdraw Successfull")

            else:
                print("Withdrawal amount exceeded")

        else:
            print("The bank is bankrupt")

    def check_balance(self):
        print(f"Your current balance is : {self.balance} tk")

    def view_transaction(self):
        for k in self.transaction:
            print(k)

    def take_loan(self, amount):
        if self.bankrupt == False:
            if Bank.is_loan:
                if self.loan_count <= 2:
                    self.loan_take += amount
                    self.add_loan(amount)
                    print(f"Loan of {amount} tk taken successfully.")
                else:
                    print("Loan limit exceeded")
            else:
                print("Loan feature is currently disabled.")
        else:
            print("The bank is bankrupt")

    def transfer(self, receiver_ac_no, amount):
        receiver = Bank.find_user_by_ac_no(receiver_ac_no)
        if receiver is None:
            print("Receiver not found!")
            return

        if self.balance >= amount:
            self.balance -= amount
            receiver.balance += amount
            self.transaction.append({"Transfer Out": amount})
            receiver.transaction.append({"Transfer In": amount})
            print(f"Successfully transferred {amount} tk to account {receiver_ac_no}")
        else:
            print("Insufficient balance for transfer!")


class Admin(Bank):
    def __init__(self, name, email, passward, address):
        super().entry_admin(self)
        self.name = name
        self.email = email
        self.address = address
        self.passward = passward

    def delete_ac(self, ac_no):
        Bank.delete_user_by_ac_no(ac_no)

    def view_all_user(self):
        print("All users in the bank:")
        for user in Bank.user_list:
            print(
                f"Name: {user.name}, Email: {user.email}, Account No: {user.ac_no}, Balance: {user.balance}"
            )


def manage_for_user(user):
    while True:
        print(
            "Tell me what do you want\n"
            "   To deposite money,press 1\n"
            "   To withdraw money,press 2\n"
            "   To check available balance,press 3\n"
            "   To check transaction history.,press 4\n"
            "   To  take a loan,press 5\n"
            "   To transfer  money,press 6\n"
            "   To exit, press 0"
        )
        op = int(input("Press option: "))
        if op == 1:
            money = int(input("Enter Amount: "))
            user.deposite(money)
        elif op == 2:
            money = int(input("Enter Amount: "))
            user.withdraw(money)
        elif op == 3:
            user.check_balance()

        elif op == 4:
            user.view_transaction()

        elif op == 5:
            money = int(input("Enter Amount: "))
            user.take_loan(money)

        elif op == 6:
            receiver_ac_no = int(input("Enter Receiver's Account Number: "))
            amount = int(input("Enter Amount to Transfer: "))
            user.transfer(receiver_ac_no, amount)

        elif op == 0:
            break


def manage_for_admin(admin):
    while True:
        print(
            "Tell me what do you want\n"
            "   To create an account, press 1\n"
            "   To delete any user account, press 2\n"
            "   To see all user accounts list, press 3\n"
            "   To check the total available balance of the bank, press 4\n"
            "   To check the total loan amount, press 5\n"
            "   To on or off the loan feature of the bank, press 6\n"
            "   To exit, press 0"
        )
        op = int(input("Press option: "))
        if op == 1:
            user = create_user()
        elif op == 2:
            ac_no = int(input("Enter the account number to delete: "))
            admin.delete_ac(ac_no)
            pass
        elif op == 3:
            admin.view_all_user()

        elif op == 4:
            Bank.check_main_balance()

        elif op == 5:
            Bank.check_loan()

        elif op == 6:
            Bank.toggle_loan_feature()
            pass

        elif op == 0:
            break


def create_user():
    Name = input("Enter your name: ")
    email = input("Enter your email: ")
    pas = input("Enter a passward: ")
    address = input("Enter your address: ")
    type = input("Account type Savings or Cuurent: ")
    user = User(Name, email, pas, address, type)
    print(
        f"\nHi, {user.name}\n"
        "Your account has been successfully created.\n"
        f"Your account number is : {user.ac_no}\n"
        "Please make sure you correctly remember this account number and passward."
    )
    return user


print(
    "\nWelcome to Islami Bank..\n"
    "   where every transaction is Shariah-compliant\n"
    "   Ensuring ethical, transparent, and faith-driven\n"
    "   financial solutions for your prosperity!"
)
while True:
    print("Tell me who you are.")
    op = int(
        input(
            "\tTo enter as a user, press 1\n"
            "\tTo enter as a Admin, press 2\n"
            "\tTo exit, press 0\n"
        )
    )
    if op == 1:
        while True:
            use = int(
                input("Press 1, for login\nPress 2, for sign up\nPress 0, for exit\n")
            )
            if use == 1:
                ac = int(input("Please Enter your account no: "))
                fnd = Bank.find_user_by_ac_no(ac)
                if fnd is None:
                    print("Receiver not found!")
                else:
                    pas = input("Enter your password: ")
                    if pas == fnd.passward:
                        print(f"Welcome {fnd.name}")
                        manage_for_user(fnd)
                    else:
                        print("Incorrect Password")

            elif use == 2:
                user = create_user()
                manage_for_user(user)
                continue
            elif use == 0:
                break

            else:
                print("Please Enter a valid operation")

    if op == 2:
        boss = Admin("Al Jabir", "jabir@gmail.com", "jabir@1234", "dhaka")
        boss2 = Admin("Rakib", "rakib@gmail.com", "rakib@1234", "satkhira")
        print("Login:")
        em = input("Enter your email: ")
        admin = Bank.find_admin(em)
        if admin is None:
            print("Admin not found!")
        else:
            pas = input("Enter your password: ")
            if pas == admin.passward:
                print(f"Welcome {admin.name}")
                manage_for_admin(admin)
            else:
                print("Incorrect Password")
