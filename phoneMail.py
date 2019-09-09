import pyperclip,re

phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))?
(\s|-)?
(\d{3})
(\s|-)
(\d{4})
)''',re.VERBOSE)

text='My phone no is: (244) 571-2963 and Shloka\'s contact id is: 408-380-1318'
phoneNo = phoneRegex.findall(text)
list=[]
for i in range(len(phoneNo)):
    list.append(phoneNo[1][0])
print(list)
copyData= pyperclip.copy(" ".join(list))
if copyData!="":
    print("Data copied to clipboard successfully")
