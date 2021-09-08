n=int(input("Enter a number"))
def isEven(num):   
        if num%2==0:
            return True
        return False
count=0
for i in range(2,n+1):
    if isEven(i):
        print(i,end=' ')
        count+=1
print("\nevens in between 50 is:",count)       
    
