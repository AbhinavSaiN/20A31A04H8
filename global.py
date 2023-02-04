def outf():#8
    var=10#1
    def innf():#2
        var=20#6
        print('inner var',var)#3
    innf()#4
    print("outer var",var)#5
outf()#7
    