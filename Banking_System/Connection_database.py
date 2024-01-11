import sqlite3

class Connection:
    def __init__(self):
        self.conn = sqlite3.connect('sql.db')
        self.cursor = self.conn.cursor()
        print('Connected!')

    def create_table(self):
        try:
            self.cursor.execute("CREATE TABLE banking (account_id VARCHAR UNIQUE KEY NOT NULL,customer_id varchar(10),name varchar(255),email varchar(255),phone_num INT,account_num INT);")
        except sqlite3.Error as e:
            print("Error :",e)

    def insert_table(self,account_id, customer_id, name, email, phone_num,account_num):
        try:
            self.cursor.execute("INSERT INTO Customers (account_id, customer_id, name, email, phone_num) "
                                "VALUES ("+ account_id + "," +customer_id + "," + name +"," + email + ","+ phone_num +","+ account_num +");")
        except sqlite3.Error as e:
            print("Error :",e)