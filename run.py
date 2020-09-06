from user import User
from credentials import Credentials
import random

#algorithms to add the credentilas as a user

def create_credentials(username_cred,password_cred):
    '''
    function to create a new credential
    '''
    new_credentials = Credentials (username_cred,password_cred)
    return new_credentials

def save_credentials(credentials):
    '''
    function to save new credentials
    '''
    credentials.save_credentials
    
def find_credentials(cls, username):
    '''
    function to find a credential given a username
    '''
    return Credentials.find_credentials_by_username(username)

def delete_credentials(credentials):
    '''
    function to delete a credential
    '''
    return Credentials.delete_credentials(credentials)
   
def existing_credentials(username):
    '''
    function to check if a credential exist given the username search 
    '''
    return Credentials.credentials_exists(username)

def display_credentials():
    '''
    function to display the credentials
    '''
    return Credentials.display_credentials()

def main():
    while True:
        print("PASSWORD LOCKER" + "\n"+ "*"*29 +"\n" + "To create a new acc enter :'reg' " 
              +"\n" + "To login to your account enter: 'log' " +"\n")
        sh = input("enter here: ").lower()
        
        if sh == "reg":
            print("Lets create your account" +"\n" +"Create a Username" +"\n")
            create_username = input("enter username here: "+ "\n")
            print("Create a Password" +"\n")
            create_password = input("enter password here: " + "\n")
            print("confrim your password"+"\n")
            confirm_password = input("confirm: "+"\n")
            
            while  confirm_password !=  create_password:
                print("Passwords did not match"+ "\t" + "try again")
                print("Create a Password" +"\n")
                create_password = input("enter password here: " + "\n")
                print("confrim your password"+"\n")
                confirm_password = input("confirm: "+"\n")    
           
            else:
                print(f"{create_username} You're registered" + "!"*10 +"\n" +"now lets log in"+"\n")
                login_username = input("enter username: "+ "\n")
                login_password = input("enter password: "+ "\n")
                
                while login_username != create_username and login_password is not create_password:
                    print("You entered a wrong password or username\t try again"+"\n")
                    login_username = input("enter username: "+ "\n")
                    login_password = input("enter password: "+ "\n")
                else:
                    print(f"{login_username} You're In"+ "!"*10 +"\n"+"Select 1, 2, 3, 4 or 5 to continue"+"\n")
                    while True:
                        print("1.Add New Credential"+"\n"
                              +"2.View your Credentials"+"\n"
                              +"3.Search Credential"+"\n"
                              +"4.Delete credential"+"\n"
                              +"Log Out"+ "\n")
                        selected = input("enter number: ")
                        
                        
                            
            
            
        
if __name__ == "__main__":
    main()