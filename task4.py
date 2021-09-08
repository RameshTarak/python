words=input("Enter a statment").split()
print(words)
count=0#iterate loop heren words:
for word in words:
    
    print(word,"==>",words.count(word))
