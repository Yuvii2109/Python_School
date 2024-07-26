#To display the parameters of the file object, f.

f=open("fnew.txt",'r')
print("File name is :",f.name)
print("File mode is :",f.mode)
print("File Encoding is :",f.encoding)
print("File is closed/not:",f.closed)
f.close()
print("File is closed/not:",f.closed)
