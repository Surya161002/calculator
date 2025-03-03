def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b==0:
        return "can't divide"
    return a/b

if __name__ =="__main__":
    print("welcome")
    a= int(input("enter the first value A ="))
    b= int(input("enter the value of B ="))
    operation= input("give the operations [+,-,*,/] = ")

    if (operation== "+"):
        print("value is ",add(a,b))
    elif(operation=="-"):
        print("value is ", sub(a,b))
    elif(operation =="*"):
        print("value is ",mul(a,b))
    elif(operation=="/"):
        print ("value is ",div(a,b))
    else:
        print("enter the correct value")