from db_conn import CUB
import sys
class sql_demo_practice:
    def __init__(self):
        self.db=CUB()
        self.main_menu()
    def register(self):
        email=input("Enter your email - ")
        password=input("Enter your password - ")
        response = self.db.registration(email,password)
        if response==1:
            print("Registration Successful")
        else:
            print("Registration Failed")
        sys.exit(0)
    def login(self):
        email=input("Enter your email - ")
        password=input("Enter your password - ")
        response  = self.db.login_student(email,password)
        try:
            if response[0][0]==email:
                print("Student logged in")
                print("Your Student ID is - ",response[0][1])
        except:
            print("Your username or password is incorrect")
            self.login()
        sys.exit(0)
    def main_menu(self):
        user_input=input("""1. Press 1 to register
2. Press 2 to login                 
        """)
        if(user_input==str(1)):
            self.register()
        else:
            self.login()

obj=sql_demo_practice()
