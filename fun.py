var='vijay'
def show():
    global var1
    var1='tall'
    print('in function var is',var)
show()
print('outside fun',var1)
print(var+' is '+var1)