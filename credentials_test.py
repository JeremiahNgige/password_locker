import unittest
from credentials import Credentials

class TestCredentials(unittest.TestCase):
    '''
    class to test all intances of the class Credentials
    '''
    
    
    def setUp(self):
        '''
        test to setup objects in the class 
        '''
        acc_name = input("enter username: ").casefold()
        acc_password = input("enter password: ").casefold()
    
        self.new_credentials = Credentials(acc_name, acc_password)
        
    def test_init(self):
        '''
        test to check if instances are instantiated correctly
        '''
        self.assertEqual(self.new_credentials.username_cred, "mainjunior")
        self.assertEqual(self.new_credentials.password_cred,"334455")
        
    def test_save_credentials(self):
        '''
        test to check if the accounts are saved
        '''
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)
        
    def tearDown(self):
        '''
        method to clean up after every test has been run
        '''
        Credentials.credentials_list =[]
        
    def test_save_multiple_credentials(self):
        '''
        test to make sure we can save multiple credentials
        '''
        acc_name1 = input("enter another username: ")
        acc_password1 = input("enter another password: ")
        
        self.new_credentials.save_credentials()
        test_credentials = Credentials(acc_name1,acc_password1)
        test_credentials.save_credentials()
        self.assertEqual(test_credentials.username_cred,"jane")
        self.assertEqual(test_credentials.password_cred,"111222")
        self.assertEqual(len(Credentials.credentials_list),2)
        
    def test_search_credentials(self):
        '''
        test to ensure that credentials can be found with a username
        '''
        acc_name2 = input("enter another username: ")
        acc_password2 = input("enter another password: ")
        credential_search = input("enter username to search cred: ")
        
        self.new_credentials.save_credentials()
        test_credentials = Credentials(acc_name2,acc_password2)
        test_credentials.save_credentials()     
        
        found_credential = Credentials.find_credentials_by_username(credential_search) 
        self.assertEqual(found_credential.password_cred,test_credentials.password_cred)  
        
        
if __name__ == "__main__":
    unittest.main()