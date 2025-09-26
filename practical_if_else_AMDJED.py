
firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")

if firstName and lastName:
    print('Welcome' +firstName +lastName)
else:
    print("Error: Both first name and last name must be provided !")

##3. Validate Login Credentials

Username= 'admin'
password= 'password123'

theusername=input("Enter your username: ")
thepassword=input('Enter your password: ')

if theusername== Username and thepassword== password : 
    print("Login successful.")
elif theusername != Username :
    print('Invalid username.')
elif thepassword != password :
    print('wrongpassword')
else: 
    print("error")