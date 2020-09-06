class User:
    ''' 
    class that geneartes new instances of users
    '''
    user_list = []
    
    def __init__(self, username, password):
        '''
        method to initilaise username and password
        '''
        self.username = username
        self.password = password
        
    def save_user(self):
        '''
        method to save a new user instance
        '''
        User.user_list.append(self)
        
    