x=float(input("number of rows of Matrix A :"))
y=float(input("number of columns of Matrix A:"))
v=[]
k=0
while k < x :
    s=[]
    j=0
    while j < y :
        a=int(input("Enter numbers in Rows : "))
        s.append(a)
        j += 1
    v.append(s)
    k += 1


g=float(input("number of rows of Matrix B :"))
h=float(input("number of columns of Matrix B :"))
l=[]
m=0
while m < h :
    n=[]
    o=0
    while o < g :
        t=int(input("Enter numbers in Rows : "))
        n.append(t)
        o += 1
    l.append(n)
    m += 1    


if len(v) == len(l) and len(s) == len(n) :
    u=0
    while u < len(v):
        w= 0
        while w < len(v):
            h=(v[u][w] + l[u][w])
            print(h, end=" ")
            w += 1
        u += 1    
        print ("\n")
else:
    print("Matrix can't add")