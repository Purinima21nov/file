def fun(a):
    i=1
    count=0
    while i<=a:
        if a%i==0:
            count=count+1
        i=i+1
    return count
x=fun(int(input("enter")))
def check():
    if x==2:
        print("yes")
    else:
        print("no")
check()