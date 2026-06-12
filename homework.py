deci=int(input("enter a decial number;"))
binary=" "
while deci>0:
    remainder=deci%2
    binary=str(remainder)+binary
    deci=deci//2
    print(f"the value of {deci} into binary conversion is {binary}")