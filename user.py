class User:
    ''' 
    class that geneartes new instances of users
    '''
    user = None
    
    def __init__(self, username, password):
        '''
        method to initilaise username and password
        '''
        self.username = username
        self.password = password
        
    