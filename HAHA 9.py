def check(num) :
    print("*************")
    print("Value in function check() is ",num)
    print("Id of num in function is ",id(num))
    num += 10
    print("Value in function check() is ",num)
    print("Id of num in function is ",id(num))
    print("*************")
myvalue = 100
print("Value in main function is ",myvalue)
print("Id of value in function is ",id(myvalue))
check(myvalue)
print("Value in main function is ",myvalue)
print("Id of value in function is ",id(myvalue))
