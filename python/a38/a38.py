
def permutationen(seq):
    if len(seq)>0:
        for e in seq:
            yield [e] 
            
    
        
        
if __name__ == "__main__":
    for e in permutationen([1,2,3]):
        print(e)