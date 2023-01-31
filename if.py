email="sai@gmail.com"
pwd=123
otp=1
cemail=input("enter the email:")
cpwd=int(input("enter the pwd:"))

if(email==cemail and pwd==cpwd):
    cotp=int(input("enter the pwd:"))
    if(otp==cotp):
        print("login successfully") 
    else:
        print("incorrect otp")
elif(email!=cemail and pwd==cpwd):
    print("invalid email")
elif(email==cemail and pwd!=cpwd):
    print("incorrect pwd")
elif(email!=cemail and pwd!=cpwd):
    print("login failed")