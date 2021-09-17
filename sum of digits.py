#program to print sum of digits in given string
s=input("Enter a string")
sm==0
for chr in s:
    if chr.isdigit():
        sm+=int(chr)
        print(sm)
