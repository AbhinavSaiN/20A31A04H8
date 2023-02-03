'''write a program to check whether the given input is satisfying the condition of anagram
test case-1
Input 1-LISTEN
Input 2-SILENT
Output-true
test case-2
i1=space
i2=racer
output-false'''

str1=input("enter name:")
str2=input("enter name:")
n=len(str1)
m=len(str2)
sortn=sorted(str1)
sortm=sorted(str2)
if n==m:
    if sortn==sortm:
        print("its anagram")
    else:
        print("not anagram")
else:
    print("if length differs its not anagram")