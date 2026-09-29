password = input('Create password: ')  #Asks user for password

score = 0
#Check if password has at least 8 characters
if len(password) >= 8:
    print('Password has at least 8 characters: \u2705')
    score = score + 1
else:
    print('Password must be at least, 8 characters! \u247C')

#Checks if password has Upper case letters
if any(char.isupper() for char in password):
    print('Password contains upper case letters: \u2705')
    score = score + 1
else:
    print('Password must contain upper case letters! \u247C')

#Checks if password has lower case letters
if any(char.islower() for char in password):
    print('Password contains lower case letters: \u2705')
    score = score + 1
else:
    print('Password must contain lower case letters! \u247C')

#Checks if password has numbers
if any(char.isdigit() for char in password):
    print('Password contains numbers: \u2705')
    score = score + 1
else:
    print('Password must contain a number! \u247C')

#Checks if password has special characters
if any(not char.isalnum() for char in password):
    print('Password has special character: \u2705')
    score = score + 1
else:
    print('Password must contain a special character! \u247C')

#Gives user final score out of 5
print('\nPassword Score:',score,'/5')

#Determines if password is strong, moderate or weak
if score == 5:
    print('Your Password is STRONG \u2705')
elif score >= 3:
    print('Your password is moderate. IMPROVE IT!')
else:
    print('Your Password is weak!!')