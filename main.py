import docx2txt
import re
my_text = docx2txt.process("Ankitaresume.docx")
pattern_email = re.compile(r'[a-zA-Z0-9-\.]+@[a-zA-Z-\.]*\.(com|edu|net)')
pattern_phone = re.compile(r'[789]\d{9}',re.VERBOSE)
pattern_name = re.compile('')

#_________________________________________________________________Institute________________________________
matchlist = ['Hospital','University','Institute','School','School','Academy','College'] # define all keywords that you need look up 
p_institute = re.compile('^(.*?),\s+(.*?),(.*?)\.')   # regex pattern to match
pattern_institute = [m.group(1) if any(x in m.group(1) for x in matchlist) else m.group(2) for m in re.finditer(p_institute, my_text)]
print(pattern_institute)
#________________________________________________________________________________________________________________


#pattern_institute = re.compile(r'/([A-Z][^\s,.]+[.]?\s[(]?)*(Hospital|University|Institute|Law School|College|School of|Academy)[^,\d]*(?=,|\d)/')

# pattern_phone = re.compile(r'^\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?\s*$')
matches_email  = pattern_email.finditer(my_text)
matches_phone  = pattern_phone.finditer(my_text)
matches_name = pattern_name.finditer(my_text)

#matches_institute = pattern_institute.finditer(my_text)

for match in matches_email:
    print("Email:", match.group(0))
for match in matches_phone:
    print("Phone no: ",match.group(0))
#for match in matches_name:
    #print("Name:", match.group(0))