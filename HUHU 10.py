#To illustrte seek()
#modification

f=open("fnew.txt","r")
print(f.tell())
f.seek(3)
print(f.tell())
f.seek(10)
print(f.read(6))
print(f.tell())
f.close()
