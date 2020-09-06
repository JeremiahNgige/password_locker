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
                        
                        #add a credential 
                        
                        if selected == "1":
                            while True:    
                                choice = input("Add credential: y/n"+"\n")
                                if choice == "y":
                                    username_cred = input("enter credential username: "+"\n")
                                    pwd_generate = input("Do you want a password generated for you: y/n"+"\n")
                                        
                                    if pwd_generate == "y":
                                        password_cred = random.randint(11111,111111)
                                        print (f"username: {username_cred}" + "\n" + f"password: {password_cred}"+"\n")
                                    elif pwd_generate == "n":   
                                        password_cred = input("enter credential password: ")
                                        print (f"username: {username_cred}" + "\n" + f"password: {password_cred}"+"\n")
                                    else:
                                        print("Enter with a y or n")
                                    save_credentials(create_credentials(username_cred,password_cred))
                                elif choice == "n":
                                    break
                                else:
                                    print("Enter with a y or n") 
                                    
                        #view credentials list            
                        
                        if selected == "2":
                            while True:
                                print("This are all your credentails below: ")
                                
                                if display_credentials():
                                    for credentials in display_credentials():
                                        print(f"Username: {credential.username_cred}"+"\n"
                                              +f"Password: {credential.password_cred}" +"\n")
                                        
                                else:
                                    print("\n"+ f"{login_username} you dont have any credentials saved yet"
                                          +"\n")       

                                menu = input("Go back to Menu: y/n"+"\n").casefold()
                                if menu is "y":
                                    break
                                elif menu == "n":
                                    continue
                                else:
                                    print("enter with a y or n")
                        
                        #search a credential by entering a username
                        if selected == "4":
                            while True:
                                search = input("Enter username of credential you want to delete: "+"\n")
                                
                                if credentials_exists(search):
                                    found_credential = search_credentials(search)
                                    print(f"Username: {found_credential.username_cred}"+"\n"+
                                          f"Password: {found_credential.password_cred}")
                                    delete = input("Delete it: y/n ?"+"\n").casefold()
                                    if delete == "y":
                                        delete_credentials(found_credential)
                                        print("Credential has been deleted successfully!!")
                                        break
                                    elif delete == "n":
                                        continue
                                else:
                                    print("The Searched credential does not exist")
                                    break
                                
                        #
                            
                                    

if __name__ == "__main__":
    main()