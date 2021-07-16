import re

from openpyxl.workbook import Workbook

file = "resume1.docx"

mobile_list=[]
with open(file) as f:
	for line in f:
		text=line
		phoneNumRegex = re.compile(r'[789]\d{9}',re.VERBOSE)
		for groups in phoneNumRegex.findall(text):
			#print(groups)
			mobile_list.append(groups)

print(mobile_list)
