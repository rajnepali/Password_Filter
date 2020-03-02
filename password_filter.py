#!/usr/bin/env python

__description__ = 'Password Filter'
__author__ = 'Raj Nepali (@nep_d0c)'
__version__ = '0.1'
__date__ = '02/06/2019'


import re
import sys
import time


special_chars = ["`","~","!","@","#","$","%","^","&","*","(",")","-","_","+","=","[","{","]","}","|",":",";","'","<",",",">",".","/","?"]

def check_password_complexity(password):
	'''This looks for the password that matches complexity of any three conditions mentioned below:

		Uppercase
		Lowercase
		Numbers
		Special Characters

	'''
	#does the password contain uppercase letter
	upper = re.findall(r'[A-Z]',password)
	if upper:
		hasupper = 1
	else:
		hasupper = 0
	
	#does the password contain lowercase letter
	lower = re.findall(r'[a-z]',password)

	if lower:
        	haslower = 1
	else:
		haslower = 0
	
	#does the password contain digit
	numbers = re.findall(r'[0-9]',password)
	if numbers:
		hasnumbers = 1
	else:
		hasnumbers = 0

	#does the password contain special characters
	if any(spec in password for spec in special_chars):
		special = 1
	else:
		special = 0

	#If any of the three conditions is met
	sum = hasupper + haslower + hasnumbers + special

	if (sum >= 3):
		return True

def main():
	count = 0
	start = time.time()

	if len(sys.argv) < 3:
		print("[+] Usage: python password_filter.py input_file output_file")
		exit(1)
	

	input_file = sys.argv[1]
	out_file = sys.argv[2]

	
	with open(input_file) as f:
		for password in f:
			password=password.strip() #You need to strip the password before calculating the length
			
			if(len(password) < 8):
				print("[!] Password:", password ," has Less than 8 chars, skipping.")
				continue

			try:
				print('[+] Password:', password, end=' ')
				#lets check for criteria, any three criteria

				result = check_password_complexity(password)
				if (result == True ):
					
					print('--> looks Good, adding to the file')
					count+=1
					try:
						fw =open(out_file,'a')
						fw.write(password + '\n')
						fw.close()
					except Exception as exc:
						print(str(exc))
				else:
					print(' does not meet complexity requirement, skipping')
			except Exception as e:
				print("Error: %s"%str(e))

	end=time.time()
	print("\n[+] Total run time: ",(end-start))
	print("\n[+] Total good passwords found and added to the list: ",count)

if __name__ == '__main__':
	main()
