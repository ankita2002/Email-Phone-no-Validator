import docx2txt
import re

my_text = docx2txt.process("resume1.docx")

pattern = re.compile(r'[a-zA-Z0-9-\.]+@[a-zA-Z-\.]*\.(com|edu|net|in)')

matches = pattern.finditer(my_text)

for match in matches:
    print(match.group(0))
    email = match.group(0)

#import re
#regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
#'/^(([^<>()[\]\.,;:\s@\"]+(\.[^<>()[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i'
#'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

def validate(email):
    if(re.search(pattern,email)):
        print(email, 'is correct')
    else:
        print(email, 'is invalid')

if __name__ == '__main__':
    #email = input("Enter Email Address: ")
    validate(email)
