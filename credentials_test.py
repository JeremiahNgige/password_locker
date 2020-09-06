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
        
if __name__ == "__main__":
    unittest.main()