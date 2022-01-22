def fun(a):
    f=open("delhi.txt","w")
    p=open("shimla.txt","w")
    c=open("other.txt","w")
    g=a.read()
    d=g.split("\n")
    i=0
    while i<len(d):
        if 'delhi' in d[i]:
            f.write(d[i])
            f.write("\n")
        elif 'shimla' in d[i]:
            p.write(d[i])
            p.write("\n")
        else:
            c.write(d[i])
            c.write("\n")
        i=i+1
fun(str(input("enter")))
        