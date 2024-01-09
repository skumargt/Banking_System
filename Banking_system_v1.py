import random

class Customer:
    def __init__(self):
        pass

    def create_account(self):
        # print("First Create a account !")
        self.customer_id = int(input("Enter Customer ID \n"))
        self.name = input("Enter your Name: \n")
        self.email = input("Enter your Email: \n")
        self.phone_num = input("Enter Phone Number: \n")[:9]
        self.account_id = self.name[:3] + str(self.customer_id)
        self.account_num = random.randint(10000000, 99999999)
        print("Your Account get successfully Created!")

    def show_account_details(self):
        print("Below are the Account Detail:\n")
        print(f"Cust ID: {self.customer_id}\nName : {self.name}\nEmail: {self.email}\nPhone No.: {self.phone_num}\nAccount Number: {self.account_num}")
        return self.customer_id, self.account_id, self.account_num

class Account(Customer):
    trans_list = []
    def __init__(self):
        super().__init__()
        self.balance = 10000

    def deposit(self):
        self.trans = {}
        self.amt = int(input("Enter amount you want to Deposit :\n"))
        self.balance = int(self.balance) + self.amt
        self.trans['Credited'] = self.amt
        self.trans_list.append(self.trans)
        print(f"Amount deposited : {self.amt}\n Now Current Account Balance is {self.balance}.")

    def withdraw(self):
        self.trans = {}
        self.withdrw_amt = int(input("Enter amount you want to Withdraw :\n"))
        self.balance = self.balance - self.withdrw_amt
        self.trans['Debited'] = self.withdrw_amt
        self.trans_list.append(self.trans)
        print(f"Amount Withdrawn : {self.amt}\n Now Current Account Balance is {self.balance}.")

    def get_balance(self):
        print(f"Total Balance : {self.balance}")

    def generate_account_statement(self):
        index = 0
        print(f"Account Number: {self.account_num}")
        while index < len(self.trans_list):
            for k,v in self.trans_list[index].items():
                print(str(k) +' - '+ str(v))
            index += 1

class AccountRepository:
    def save_account(self):
        print("Below are the Saving Account Detail:")
        print(f"Cust ID: {self.customer_id}\nName : {self.name}\nEmail: {self.email}\nPhone No.: {self.phone_num}\nAccount Number: {self.account_num}")

    def find_account_by_id(self, account_id):
        # we can get it by applying loop over the account id column from database
        pass

    def find_accounts_by_customer_id(self, customer_id):
        # we can get it by applying loop over the customer id column from database
        pass

class Transaction(Account,AccountRepository):
    def __init__(self):
        super().__init__()
        print("Do you want to open an account? Y/N")
        self.opt = input().capitalize()
        if self.opt == "Y":
            super().create_account()
            print("Do you want to perform any transaction : Press Y")
            self.choice = input().capitalize()
            if self.choice == "Y":
                self.trigger_action()
            else:
                exit(1)
        elif self.opt == "N":
            print("Thanks for banking!")
            exit(1)
        else:
            print("Wrong Input!")


    def make_transaction(self, account_id, trans_type, amount=0):
        if trans_type == 1:
            super().deposit()
            self.trigger_action()
        elif trans_type == 2:
            super().withdraw()
            self.trigger_action()
        elif trans_type == 3:
            super().save_account()
            self.trigger_action()
        elif trans_type == 4:
            super().generate_account_statement()
            self.trigger_action()
        elif trans_type == 5:
            super().get_balance()
            self.trigger_action()
        elif trans_type == 0:
            print("Thanks for banking!")
            exit(1)

    def trigger_action(self):
        self.trans_type = int(input("Press 1 for Deposit ,2 for Withdraw ,3 for Account Detail ,4 for Account Statement ,5 for Account Balance, 0 for Exit \n"))
        self.make_transaction(self.account_id, self.trans_type)

if __name__ == "__main__":
    obj = Transaction()

