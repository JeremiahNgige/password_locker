import unittest
from credentials import Credentials
import pyperclip

class TestCredentials(unittest.TestCase):
    '''
    class to test all intances of the class Credentials
    '''
    
    
    def setUp(self):
        '''
        test to setup objects in the class 
        '''
    
        self.new_credentials = Credentials("mainjunior", "334455")
        
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
        
        self.new_credentials.save_credentials()
        test_credentials = Credentials("mainjunior","334455")
        test_credentials.save_credentials()
        
        self.assertEqual(len(Credentials.credentials_list),2)

    def test_delete_credentials(self):
        '''
        test to ensure credentials can be deleted from credentials_list
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("mainjunior","334455")
        test_credentials.save_credentials
        
        self.new_credentials.delete_credentials
        self.assertEqual(len(Credentials.credentials_list),1)
                
    def test_search_credentials(self):
        '''
        test to ensure that credentials can be found with a username
        '''
        
        self.new_credentials.save_credentials()
        test_credentials = Credentials("mainjunior","334455")
        test_credentials.save_credentials()     
        
        found_credential = Credentials.find_credentials_by_username("mainjunior") 
        self.assertEqual(found_credential.password_cred,test_credentials.password_cred)  
    
    def test_credential_exists(self):
        '''
        test to ensure that credentials exists    
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("mainjunior","334455")  # new cred
        test_credentials.save_credentials()

        credentials_exists = Credentials.credentials_exists("mainjunior")

        self.assertTrue(credentials_exists)
        
    def test_display_credentials(self):
        '''
        method that displays all current credentials
        '''
        self.assertEqual(Credentials.display_credentials(),
                         Credentials.credentials_list)
        
if __name__ == "__main__":
    unittest.main()