s=input("enter a string:")
count=0
for ch in s:
    ch=ch.lower()
    if ((ch=="a")or(ch=="e")or(ch=="i")or(ch=="o")or(ch=="U")):
        count+=1
        print(count)
        ovelstr="aeiouAEIOU"
        count=0
        for ch in s:
            if ch in ovelstr:
                count+=1
                print(count)
