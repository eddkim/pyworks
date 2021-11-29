def sos(n):
    for i in range(n):
        print("Help me")

def sos2(n):
    print("help me")
    if n <=1:
        return n
    else :
        return sos2(n-1)

sos(5)