import sys

def ggT(x,y):
    print(x,y)
    if (x == y):
        return x
    
    if x>y:
        x = ggT(x-y, y)
    
    else:
        x = ggT(y,x)
        
    return x
        
    
if __name__ == "__main__":

    print("ggT",ggT(20,30))
    print(sys.version)