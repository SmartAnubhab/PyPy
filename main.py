print('LogIn form')

username=input('Please enter your user name\n')
password=input('Please enter your password\n')

hidden_pw=len(password)*'*'
#print('hey {}  your password {} is {} characters long '
#.format(username, hidden_pw, len(password) ))

print(f'hey {username}, your password {hidden_pw} is {len(password)} characters long ')



