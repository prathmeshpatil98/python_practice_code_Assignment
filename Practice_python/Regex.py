import re

data =  " Myself Prathmesh Patil , My Favourite date is 6 feb 2002 #AI"
# pattern1 = re.compile(r'[A-Za-z\d]+')
pattern1 = re.compile(r'\d{3}')

output = re.findall(pattern1,data)

print(output)

