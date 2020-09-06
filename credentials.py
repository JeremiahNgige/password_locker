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
        
    def save_credentials(self):
        '''
        method to save the accounts
        '''
        Credentials.credentials_list.append(self)
        
    @classmethod   
    def find_credentials_by_username(cls,username):
        '''
        method to search a credentials in credentials_list by the username
        
        arg:
            cls is the to make the class an argument and username to take in 
            a username as the argument
        '''
        
        for credential in cls.credentials_list:
            if credential.username_cred == username:
                return credential
            