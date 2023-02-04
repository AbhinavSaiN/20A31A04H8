'''class abc:
    attribute=10
obj=abc()
print(obj.attribute)'''

class abc:
    def __init__(self,value):
        print("this is in class")
        self.value= value
        print("the value is", value)
obj=abc(100)