# This project is for a user to check if their passowrd against basic criteria which will ultimately determine whether or not it is strong enough.
# If the user's password passes the check, the user then has the option to encrypt their password which will be salted and encrypted with base64 encryption
# This project was developed by Long3eard © 2024


# ------------------------------------------------


# import the re module to search through the content
import re
import base64

# place everything within a function
def passcode():

# define variables
	pswd = input('Please enter your password? ')
	pswd_salt = pswd + "*D465168@#$@!" 
	pswd_bytes = pswd_salt.encode("ascii")
	pswd_base64 = base64.b64encode(pswd_bytes)
	flag = 0

# -------------------------------------------------------------

# create a while loop to iterate input through
	while True:
		if (len(pswd)<=8):
			flag = -1
			break
		elif not re.search("[a-z]", pswd):
			flag = -1
			break
		elif not re.search("[A-Z]", pswd):
			flag = -1
			break
		elif not re.search("[0-9]", pswd):
			flag = -1
			break
		elif not re.search("[!@#$%^&*]", pswd):
			flag = -1
			break
		elif re.search("\s", pswd):
			flag = -1
			break
		else:
			flag = 0
			print("Valid password")
			break
# -------------------------------------------------------------

# if the inputted password does not meet the above criteria then it will fail 
	if flag == -1:
		print("Not a valid password, please try again")
		
# if the password meets the criteria, then the user as the option to encrypt their password
	if flag == 0:
		salt = input("Would you like to encrypt your password? ").lower()
		if salt in ['yes', 'y']:
			print(f"Your encoded password is: {pswd_base64.decode('ascii')}")
		else:
			print("Password encyrption skipped.")

# -------------------------------------------------------------

# call the function
passcode()
