n=int(input("Enter the number: "))
flag=0
for i in range(2,n):
    if n%i==0:
        flag=1
        break
    else:
        x=n
        sum=0
        while x>0:
            r=x%10
            sum=sum*10+r
            x=x//10
if sum==n:
    print(n,"is a prime pallindrome")
else:
    print(n,"is not a prime pallindrome")   
