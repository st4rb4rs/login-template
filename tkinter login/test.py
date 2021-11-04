import logins

new_user = input('New Username: ')

for i in range(len(logins.users)):
        if new_user == logins.users[i]:
            print('Username taken, try something different')