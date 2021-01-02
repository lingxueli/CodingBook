username = input('enter the username: ') # ask for useranme
password = input('enter the password: ') # ask for password


print(f'{username}, your password {password} is {len(password)} letters long')

pwd_length = len(password)
hidden_password = '*' * pwd_length

print(f'{username}, your password {hidden_password} is {pwd_length} letters long')
