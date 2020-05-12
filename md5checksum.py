import hashlib
userinput =input("enter file name : ")
hasher =hashlib.md5()
with open(userinput,"r") as f:
    content=f.read()
    hasher.update((content).encode('utf-8'))
    a=hasher.hexdigest()
    print(a)

userinput =input("enter file name : ")
hasher =hashlib.md5()
with open(userinput,"r") as f:
    content=f.read()
    hasher.update((content).encode('utf-8'))
    b=hasher.hexdigest()
    print(b)

if a==b:
    print("files mached")