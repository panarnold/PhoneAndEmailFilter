#! python
# it find phone numbers and email addresses from the clipboard in a second
# Arnold Cytrowski X 2020

import pyperclip, re

phone_regex = re.compile(r'''(
(\d{3}|\(\d{3}\))? #dialling code
(\s|-|\.)? # 1st separator
(\d{3}) #first three digits
(\s|-|\.) #separator
(\d{4}) # last four digit
(\s*(ext|x|ext.)\s*(\d{2,5}))? # internal number
)''', re.VERBOSE)

email_regex  = re.compile(r'''(
[a-zA-Z0-9._%+-]+ #user name
@ #it's obvious, isnt it?
[a-zA-Z0-9.-]+ #domain name
(\.[a-zA-Z]{2,3}) #dot ant the rest, two to three lethers, greedy style
)''', re.VERBOSE)

text = str(pyperclip.paste())
matches = []
for groups in phone_regex.findall(text):
    phone_num = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phone_num += ' x' + groups[8]
    matches.append(phone_num)
for groups in email_regex.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('data has been copied into clipboard, sir.')
    print('\n'.join(matches))
else:
    print("There are not any email addresses or phone numbers in the clipboard, sir")
