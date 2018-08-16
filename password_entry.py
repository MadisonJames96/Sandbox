MIN_LENGTH = 2
password = input("Password: ")

if len(password) < MIN_LENGTH:
    print("password to short")
    print("try again")
    password = input("Password: ")
else:
    password_length = len(password)
    for i in range (password_length):
        print('*', end=' ')
print()