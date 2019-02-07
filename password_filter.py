#!/usr/bin/python

__description__ = 'Password Filter'
__author__ = 'Raj Nepali (@nep_d0c)'
__version__ = '0.1'
__date__ = '02/06/2019'


import re
import sys
import time

#list of special chars, I went this route since I was having trouble matching regex
special_chars = ["!","@","#","$","%","^","&","*","(",")","/","?",".",","]


def check_password_complexity(password):
	#does the password contain uppercase letter
	upper = re.findall(r'[A-Z]',password)
        if upper:
        	hasupper=1
        else:
        	hasupper=0
	#does the password contain lowercase letter
        lower = re.findall(r'[a-z]',password)
        if lower:
        	haslower=1
        else:
        	haslower=0
	#does the password contain digit
        numbers=re.findall(r'[0-9]',password)
        if numbers:
        	hasnumbers=1
      	else:
        	hasnumbers=0
        #this regular expression only matches if it has letters and numbers,otherwise it has special characters, tested on regex101
        #if re.match("^[a-zA-Z0-9_]*$",password):
        #       special = 0
        #else:
        #       special = 1
        #But i decided to use list, i was getting false positives, maybe I can find better regex

        if any(spec in password for spec in special_chars):
        	special = 1
        else:
        	special = 0
        sum = hasupper+haslower+hasnumbers+special

	#if the password matches any three criteria
	if (sum >=3):
		return 1
	else:
		return 0


def main():
	count=0

	if len(sys.argv) != 3:
		print "[+] Usage: python clean.py input_file output_file"
		exit(1)

	input_file = sys.argv[1]
	out_file = sys.argv[2]

	start = time.time()
	with open(input_file) as f:
		for password in f:
			password.strip() #You need to strip the password before calculating the length
			if(len(password) < 9):
				#For some reason, It is reading extra bit, will test this later
				print "[!] Password:",password,
				print " has Less than 8 chars, skipping"
				continue

			#if password contains more than two consecutive letters, ignore and move on
			# Lets use regular expression to test for three consecutive letters
			substr = re.search(r'([a-z\d])\1\1',password) #not optimal, but works :)
			#print substr.group(0)
                	if (substr):
				print password, " contains Consecutive characters, skipping"
				continue
			try:
				print "[+] Working on password:", password,
				#lets check for criteria, any three criteria

				result = check_password_complexity(password)
      				if (result ==1 ):
					print "--> looks Good, adding to the file"
					count+=1
              				try:
						fw =open(out_file,'a')
						fw.write(password)
						fw.close()
					except Exception as exc:
						print str(exc)
				else:
					print password, " does not meet complexity requirement, skipping"
    			except Exception as e:
				print "Error: %s"%str(e)

	end=time.time()
	print "\n[+] Total run time: ",(end-start)
	print "\n[+] Total good passwords found and added to the list: ",count

if __name__ == '__main__':
	main()

