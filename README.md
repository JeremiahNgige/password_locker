# Password Locker App

Author Jeremiah Ngige.

## Description

This is an application to help manage passwords of given credentials given their usernames too.

### Installation

* Clone this repository locally on your computer.
* Ensure you have python3.8 installed in your computer.
* From the terminal navigate to the cloned project folder.
* Run python3.8 run.py code in the terminal to launch the app.

## How to Use The app

* Once you launch, You can either create a new user, or login  
* If you choose to login(log), use: user1 as username and 123 as passWord
* If you choose to create a new account, use reg as the code and follow the prompts.
* Once logged in, you can:

1. Add Credentials.
2. View saved Credentials.
3. Search Credentials.
4. Delete credentials.
5. Log Out.

### Running unit tests

* Run python3.8 credentials_test.py for credential class tests.
* Run python3.8 user_test.py for user class tests.

## Issues

Since there is no database to support the app, once you exit or log out of a session you loose all the credentials and created user. You have to create a new user for every session. You can still use the default login but if you exit the app, you will still loose all the credentials you created.

## Technologies used

 Python 3.8
 PyperClip

## License

licensed under the [MIT license](LICENSE).
