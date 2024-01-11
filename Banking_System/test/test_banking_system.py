import unittest
import sys

sys.path.insert(1, '..\Domain')
sys.path.insert(1, '..\Service')
sys.path.insert(1, '..\Infra')
from create_account import CustomerAccount
from transactions import AccountTransaction
from account_repository import AccountRepository

class TestAccountCreation(unittest.TestCase):

    def setUp(self) -> None:
        self.customer_id = "101"
        self.name = "John Wick"
        self.email = "john.wich@gmail.com"
        self.phone_num = 1490292929
        self.balance = 10000

    # def tearDown(self) -> None:
    #     print("Thanks for using Banking System!")

    def test_create_account(self):
        # print(CustomerAccount.create_account(self.customer_id,self.name,self.email,self.phone_num))
        self.assertTrue(CustomerAccount.create_account(self.customer_id,self.name,self.email,self.phone_num))

    def test_transactions(self):
        obj = AccountTransaction(self.balance)
        self.assertTrue(obj.deposit(5000))
        self.assertTrue(obj.withdraw(1000))
        # self.assertRaises(Exception,obj.withdraw,10600)
        self.assertTrue(obj.get_balance(self.customer_id))
        self.assertTrue(obj.generate_account_statement(self.customer_id))


if __name__ == "__main__":
    unittest.main()