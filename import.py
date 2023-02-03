import re
str='she sells sea shells at sea shore'
p1='sells'
if re.search(p1,str):
    print("match found")
else:
    print(p1,"not present in string")
    
    
import re
str='she sells sea shells at sea shore'
p1='sea'
rep='ocean'
ns=re.sub(p1,rep,str,1)
print(ns)