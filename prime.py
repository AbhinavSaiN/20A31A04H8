num=int(input("enter number:"))
case = False

if num == 1:
    print(num, "is not a prime number")
elif num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            case = True
            break

    if case:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")
