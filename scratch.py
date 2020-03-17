#Bin to ip4
z=0
q=input("Do you want to convert an IPv4 or IPv6 to binary? ")
a=-1
b=-1
def conv(q):
    if q == "IPv4":
        a=input("Enter an IPv4 address without any periods and it will convert to binary: ")
        z=int a
        return bin(int(a))[2:]
    elif q=="IPv6":
        b=input("Enter an IPv6 address without any periods and it will convert to binary: ")
        b.replace("a",10).replace("b",11).replace("c",12).replace("d",13).replace("e",14).replace("f",15)
        return bin(int(b))
    else:
        q=input("Type in IPv4 or IPv6: ")
        return conv(q)

print(conv(q))