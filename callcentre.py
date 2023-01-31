calls=3000
ccalls=int(input("enter the number of calls:"))
data=2.0
cdata=float(input("enter the data used:"))
msg=100
cmsg=int(input("enter the msg sent:"))
days=84
cdays=int(input("enter the day:"))
recharge=days-cdays
print(recharge)
if(days>=cdays):
    print("no. of remaining days left",recharge)
    if(calls<ccalls):
        print("kindly top-up")
        if(data<cdata):
            print("no data available")
            if(msg<cmsg):
                print("message not sent")