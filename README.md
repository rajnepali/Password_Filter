# Password_Filter
A lot of time, you are faced with the challenge to brute force password on the systems that have some complexity rules (most systems these days). There are a lot of password lists available (rockyou.txt, password.lst from john and other leaked passwords,e.g. SecLists), however most of them have very generic and common passwords that does not meet complexity requirements and you end up making your attack noisy and lengthy.

Password_Filter is a small tool that takes passwords lists/file as input and filters the password that matches the complexity rules.
I used this for my project and hopefully this would be useful for others. I will work on this more if there is interest.

Good for both Red Team and Blue Team :)

Examples:
python3 password_filter.py -L10 -UlSN -i /home/titan/Desktop/passwords/ -o output.txt
