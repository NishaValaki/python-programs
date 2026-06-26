n1=10
n2=50
op= "*"
match op:
    case"+":
        c=n1+n2
        print("sum is",c)
    case"-":
        c=n1-n2
        print("sum is",c)
    case"*":
        c=n1*n2
        print("multiplication is",c)
    case"/":
        c=n1/n2
        print("division is",c)
    case _:
        print("select + - * /")