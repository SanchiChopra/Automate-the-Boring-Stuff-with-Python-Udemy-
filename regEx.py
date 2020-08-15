import re
message = "Call me at 415-555-1011 tomorrow, or at 415-555-9999"

phoneNumRegEx = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegEx.search(message)
print(mo.group())

'''
To find all occurrences of the given pattern:
phoneNumRegEx = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(phoneNumRegEx.findall(message))      (returns list of all matched expressions)
# '''
