def ggT(x,y):
    while(x != y):
        if x>y:
            x = x-y 
        else:
            x,y = y,x 
    return x 

def ggTl(x,y, *z):
    if not z:
        return ggT(x,y)
    
    else:
       x = ggT(x,y)
       
    for e in z:
        x = ggT(x,e)
    return x
    
def ggTOfFile():
    f = open('a30-ggts.dat','r')
    i = 0
    sum = 0
    anzahlGGT = 0
    y = 'undefined'
    
    for e in f:
        if i<=1:
            if i == 0:
                x = int(e)
            if i == 1:
                y = int(e)
                sum+= ggT(x,y)    
                anzahlGGT +=1
                
        else:   
            if i % 2 == 0:
                x = int(e)
            else:
                y = int(e)
                sum+= ggT(x,y)
                anzahlGGT+=1    
        i+=1
        
    midGGT = sum/anzahlGGT
    print("mid ggt:", midGGT)
    
if __name__ == "__main__":
    #print(ggT(8,6))
    print(ggTl(7,2,2,1,20,11))
    print(ggTOfFile())
    