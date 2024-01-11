import random

class CustomerAccount:

    # This below function takes input as cutomer_id,name,email,phone number and returns Account number and account ID
    def create_account(customer_id, name, email, phone_num):
        try:
            account_id = name[:3] + str(customer_id)
            account_num = random.randint(10000000, 99999999)
            print("Your Account get successfully Created!")
            return account_id, account_num
        except Exception as e:
            print("Error happened :",e)
            return False
