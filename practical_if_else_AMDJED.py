UserFirstname= 'Amdjed'
Userlastname= 'Meghezzi'

firstName=input('Enter your firstName : ')
lastName=input('Enter your lastName : ')

if firstName == UserFirstname and lastName == Userlastname:
    print('welcome, ' + firstName , lastName)
elif firstName == "" or lastName == "":
    print("Error: Both first name and last name must be provided.")    
else:
    print('Please Check Your Information ! ')
    