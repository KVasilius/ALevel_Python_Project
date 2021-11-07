import sqlite3

connection_details = sqlite3.connect("bank_details.db")
cur = connection_details.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS details(id intiger UNIQUE, balance intiger)""")

class Bank_info:

    def __init__(self):
        self.name = int(input("enter acct num: "))
        self.check()

    def check(self):
        cur.execute("""SELECT * from details where id = :id""", {"id":self.name}) 
        if cur.fetchone() != None: 
            self.use = input("withdraw, deposit or check balance: ")
            if self.use == "withdraw": self.withdraw()
            elif self.use == "deposit": self.deposit() 
            elif self.use == "check balance" or self.use == "check": self.get_balance()
        else:
            print("no such account")
            exit

    def withdraw(self):
        self.ammount = int(input("how much money to withdraw: "))
        cur.execute("""SELECT balance FROM details WHERE id = :id""", {"id":self.name})
        balance = cur.fetchone()
        if balance[0] >= self.ammount:
            cur.execute("""UPDATE details SET balance = :new_ammount WHERE id = :id""", {"new_ammount":balance[0]-self.ammount,"id":self.name})
            self.get_balance()
        else: 
            print("not enoght funds")

    def deposit(self):
        self.ammount = int(input("how much money to deposit: "))
        cur.execute("""SELECT balance FROM details WHERE id = :id""", {"id":self.name})
        balance = cur.fetchone()
        cur.execute("""UPDATE details SET balance = :new_ammount WHERE id = :id""", {"new_ammount":balance[0]+self.ammount,"id":self.name})
        self.get_balance()

    def get_balance(self):
        cur.execute("""SELECT balance FROM details WHERE id = :id""", {"id":self.name})
        print("balance is", cur.fetchone()[0])

acct_action = input("Create or login account: ")
while acct_action != "login" and acct_action !=  "create": acct_action = input("Wrong try again \nCreate or login account: ")
while True:
    if acct_action == "create":
        cur.execute("""INSERT INTO details (balance) VALUES (0)""")
        cur.execute("""SELECT last_insert_rowid() """)
        print("Your account number is",cur.fetchone()[0])
        connection_details.commit()
        acct_action = input("Create or login account: ")
    elif acct_action == "login": b = Bank_info()



