#Login details stored in database
stored_username = 'Kelvin'
stored_password = 'KelvinAsam123'

logged_in = False
attempts = 0
max_attempts = 3


while not logged_in and attempts < max_attempts:

 username = input('Enter username: ')
 password = input('Enter password(At least 8 characters): ')

 #Checks lenth of password
 if len(password) < 8:
    print('Password must be at least, 8 characters! \u247C')
 else:
    print('Password has at least 8 characters: \u2705')

 #Checks if user input matches stored credentials in database
 if username == stored_username and password == stored_password:
    print('Login successful\nAccess granted \u2705')

    logged_in = True

 else:
   attempts = attempts + 1
   attempts_remaining = max_attempts - attempts
   print('Login failed \u247C')

 #Prints number of attempts remaining
   if attempts_remaining > 0:
    print('Attempts remaining: ',attempts_remaining)

 #Locks account after 3 failed attempts
 if attempts == max_attempts and not logged_in:
  print("Account locked.")
  print("Too many failed login attempts. \u247C")
  