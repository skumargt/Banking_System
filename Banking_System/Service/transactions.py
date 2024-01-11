
import time

class AccountTransaction:
    trans_list = []
    def __init__(self,balance):
        self.balance = balance

    # This method is used to deposit a sum of amount to current balance of specific account.
    def deposit(self,amount):
        trans = {}
        try:
            self.balance = int(self.balance) + amount
            dtime = str(time.ctime())
            trans[dtime + ' - Credited'] = amount
            self.trans_list.append(trans)
            print(f"Amount deposited : {amount}\n Now Current Account Balance is {self.balance}.")
            return self.balance
        except Exception as e:
            print("Error happened during deposit :", e)
            return False

    # This method is used to perfrom withdrawl from account maintaing all checks (No negative balance).
    def withdraw(self,amount):
        trans = {}
        try:
            if self.balance > 0 and self.balance > amount:
                self.balance = self.balance - amount
                wtime = str(time.ctime())
                trans[wtime + ' - Debited'] = amount
                self.trans_list.append(trans)
                print(f"Amount Withdrawn : {amount}\nNow Current Balance is {self.balance}.")
                return self.balance
            else:
                raise Exception("Insufficient Balance!")
        except Exception as e:
            print("Error happened during withdrawn :", e)
            raise Exception("Insufficient balance to withdraw!")

    # This method is to show current total Balance in account by taking customer ID(Unique) as input.
    def get_balance(self, customer_id):
        if self.balance >= 0:
            print(f"Total Balance : {self.balance}")
            return self.balance
        else:
            return "Insufficient Balance"

    # This method is used to generate the account statement by taking customer ID(Unique) as input
    def generate_account_statement(self, customer_id):
        index = 0
        try:
            if self.trans_list:
                while index < len(self.trans_list):
                    for k,v in self.trans_list[index].items():
                        print(str(k) +' - '+ str(v))
                    index += 1
                return True
            else:
                return False
        except Exception as e:
            print("Sorry for Inconvience to generate account statement!")
            return False