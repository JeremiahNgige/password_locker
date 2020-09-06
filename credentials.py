class Credentials:
    '''
    class that generates new instances of user accounts credentials
    '''
    credentials_list = []
    
    def __init__(self,username_cred,password_cred):
        '''
        method to intialise the username and password cred of an account
        '''
        self.username_cred = username_cred
        self.password_cred = password_cred
        