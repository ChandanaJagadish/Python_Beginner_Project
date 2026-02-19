import re
import pyperclip
phn=re.compile(r'''(
    (\d{3}|\(\d{3}\))?
    (\s|-|\.)?
    (\d{3})
    (\s|-|\.)
    (\d{4}))''',re.VERBOSE)
email=re.compile(r'''(
    [a-zA-Z0-9._%+-]+
    @
    [a-zA-Z0-9.-]+
    (\.[a-zA-Z]{2,4})
    )''',re.VERBOSE)
text=str(pyperclip.paste())
matches=[]
for i in phn.findall(text):
    phn_re='-'.join([i[1],i[3],i[5]])
    matches.append(phn_re)
for i in email.findall(text):
    matches.append(i[0])
if len(matches)>0:
    pyperclip.copy('\n'.join(matches))
    print('copied to clipboard')
    print('\n'.join(matches))
    
    