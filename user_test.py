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
        x = input("enter your username: ")
        y = input("enter password: ")
        
        self.new_user = User(x,y)
        
    def test_init(self):
        '''
        test if user credentials are instantiated correctly
        '''
        self.assertEqual(self.new_user.username,"johndoe")
        self.assertEqual(self.new_user.password,"232323")
        
if __name__ == "__main__":
    unittest.main()