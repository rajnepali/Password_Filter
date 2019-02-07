# Password_Filter
A lot of time increasingly, you are faced with the challenge to brute force password on the systems that have some complexity rules. There are a lot of password dumps (rockyou.txt, password.lst from john and other loaked passwords), however most of them have very generic and common passwords that does not meet complexity requirements and you end up making your attack noisy and lengthy. So, a tool might be handy where you can define creteria to filter passwords from these list to come up with a filtered/curated password list.

Password_Filter is a small tool that takes passwords file as input and filters the password that matches the complexity rules.
Hopefully, this would be useful for others. I will work on this more if there is interest.

Good for both Red Team and Blue Team :)

Examples:
./password_filter.py rockyou.txt out.txt
