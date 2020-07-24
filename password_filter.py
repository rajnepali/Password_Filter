#!/usr/bin/env python

__description__ = 'Password Filter'
__author__ = 'Raj Nepali (@nep_d0c)'
__version__ = '0.2'
__date__ = '07/23/2020'


import os
import re
import sys
import time
import argparse
from os import walk

CONDITION = 0

special_chars = ["`","~","!","@","#","$","%","^","&","*","(",")","-","_","+","=","[","{","]","}","|",":",";","'","<",",",">",".","/","?"]


def check_password_complexity(password, args):
	global CONDITION
	hasupper = 0
	haslower = 0
	hasnumbers = 0
	hasspecial = 0
	#does the password contain uppercase letter
	if args.U:
		upper = re.findall(r'[A-Z]',password)
		if upper:
			hasupper = 1
			
	if args.l:
		lower = re.findall(r'[a-z]',password)
		if lower:
			haslower = 1

	#does the password contain digit
	if args.N:
		numbers = re.findall(r'[0-9]',password)
		if numbers:
			hasnumbers = 1

	#does the password contain special characters
	if args.S:
		if any(spec in password for spec in special_chars):
			hasspecial = 1

	#If any of the three conditions is met
	total = hasupper + haslower + hasnumbers + hasspecial

	if (total >= CONDITION):
		return True


def main():
	count = 0
	start = time.time()
	global CONDITION

	if len(sys.argv) < 4:
		print("[+] Usage: python password_filter.py -L [-U] [-l] [-N] [-S] -i input_file -o output_file")
		exit(1)
	

	parser = argparse.ArgumentParser(description='Password - Filter')
	parser.add_argument('-L', help='Length of passwords')
	parser.add_argument('-U', help='Uppercase Character', action="store_true")
	parser.add_argument('-l', help='Lowercase Character', action = "store_true")
	parser.add_argument('-S', help='Special Character', action = "store_true")
	parser.add_argument('-N', help='Numbers', action = "store_true")
	parser.add_argument('-i', help='Input File')
	parser.add_argument('-o', help='Output File')


	args = parser.parse_args()

	input_path = args.i
	input_file = []
	out_file = args.o
	length = int(args.L)

	CONDITION = sum(bool(x) for x in [args.U,args.l,args.N,args.S])

	print(f"[+] Password will satisfy criteria if at least {CONDITION+1} conditions match")


	if os.path.isdir(input_path):
		files = []
		for (dirpath, dirnames, filenames) in walk(input_path):
			files.extend(filenames)
			break
		for i in files:
			input_file.append(input_path+i)
	elif os.path.isfile(input_path):
		input_file.append(input_path)
	else:
		print("[!] Please enter a valid file or a directory")


	for file in (input_file):
		print(f"\n[->] Opening {file} to read")
		with open(file) as f:
			for password in f:
				password=password.strip() #You need to strip the password before calculating the length
			
				if(len(password) < length):
					print(f"[!] Password: {password} has Less than {length} chars, skipping.")
					continue

				try:
					print('[+] Password:', password, end=' ')
					#lets check for criteria, any three criteria

					result = check_password_complexity(password, args)
				
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
	print("[+] Total good passwords found and added to the list: ",count)


if __name__ == '__main__':
	main()
