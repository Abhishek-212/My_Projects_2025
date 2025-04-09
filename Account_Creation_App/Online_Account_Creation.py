# Q4) Login 
import os
import json

class Insta:
    def __init__(self):
        self.SeenUser = {}
        #self.fileName = "user_data.json"
        self.LoadUser()
    
    # Loading / reading user data from file 
    def LoadUser(self):
        if os.path.exists("user_data.json"):
            with open("user_data.json","r") as file:
                self.SeenUser = json.load(file)
        else:
            self.SeenUser = {}
    # Saving / writes user data into file        
    def SaveUser(self):
        with open("user_data.json", "w") as file:
            json.dump(self.SeenUser, file)
            
    def SignUp(self):
        username = input("Create Username: ")
        if username in self.SeenUser:
            print("User already Exists, try to Login..")
            return
        password = input("Create Password: ")
        self.SeenUser[username] = password
        self.SaveUser()
        print("Account created successfully..")
        
    def Login(self):
        username = input("Enter username: ")
        password = input("Enter Password: ")
        if username in self.SeenUser and self.SeenUser[username] == password:
            print("Login successfully...")
        else:
            print("Wrong username or password..!")
            
    def UpdatePass(self):
        username = input("Enter username: ")
        if username not in self.SeenUser:
            print("No user found..!")
            return
        oldPass = input("Enter Old Password: ")
        if self.SeenUser[username] == oldPass:
            newPass = input("Enter New Password: ")
            self.SeenUser[username] = newPass
            self.SaveUser()
            print("Password Changed Successfully...")
        else:
            print("Old Password is incorrect...")
            
#----------------------------------
# Main Program
#----------------------------------

def main():
    details = Insta()
    
    
    choice = int(input("1 for Login\n2 for Sign up\n3 for Change Password\n"))
    if choice == 1:
        details.Login()
    elif choice == 2:
        details.SignUp()
    elif choice == 3:
        details.UpdatePass()
    else:
        print("Wrong input... Try again..\n\n")
    
# Run program
main()