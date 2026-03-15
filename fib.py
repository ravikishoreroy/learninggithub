n=int(input("enter the number : "))
n1=0
n2=1
print(n1,end=" ")
print(n2,end=" ")
for i in range(0,n):
    print(n1+n2,end=" ")
    temp=n1
    n1=n2
    n2=temp+n2