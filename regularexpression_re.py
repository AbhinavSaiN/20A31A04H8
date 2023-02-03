import re
p=r'[aeiou]'
if re.search(p,'clue'):
    print('matchy vowel')
else:
    print('no vowel')