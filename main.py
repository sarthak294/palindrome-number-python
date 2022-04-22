n=int(input("Enter no. to check if it is pallidrom "))
o=n
i=0
while(n!=0):
    y=n%10
    i=i*10+y
    n=n//10
print("The no. reversed is ",i)
if(o==i):
       print("no. is pallindrom ")
else:
    print("no. is not pallindrom")