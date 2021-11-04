from getpass import getpass
import time
import logins

username = input('Username: ')
password = input('Password: ')

print('Logging In...')
time.sleep(1)

def check_login(user, pasw):
    if user in logins.users and pasw in logins.passes:
        print('Valid')
    else:
        print('Invalid user and password, try again.')


check_login(username, password)