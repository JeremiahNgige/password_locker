import unittest
from user import User

class TestUser(unittest.TestCase):
    '''
    class to test every instance of the user class
    '''
    def setUp(self):
        '''
        method to create an instance of a user to test
        '''
        self.new_user = User("johndoe","232323")
        
    def test_init(self):
        '''
        test if user credentials are instantiated correctly
        '''
        self.assertEqual(self.new_user.username,"johndoe")
        self.assertEqual(self.new_user.password,"232323")
        
    def test_save_user(self):
        '''
        test to check if user can be saved
        '''
        self.new_user.save_user()
        self.assertEqual(len(self.new_user.user_list),1)
        
        
if __name__ == "__main__":
    unittest.main()