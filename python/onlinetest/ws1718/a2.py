'''
Created on 09.02.2019

@author: domee
'''

class Ernte():
    
    def __init__(self, *files):
        self.input = []

        if len(files) == 1:
            f = open(*files)
            for line in f:
                self.input.extend(line.split())

        else:
            for f in files:
                file = open(f)
                for f in file:
                    f = f.split()
                    self.input.extend(f)
        
        self.processInput()
        self.vegs = self.findVegs()

        
    def processInput(self):
        lis = []
        for e in self.input:
            if e[-1] in ".:,!?":             
                new = e[:-1]
                lis.append(new)
            else:
                lis.append(e)
                
        self.input = lis
        
    def findVegs(self):
        vegs = {}
        pre = '#'
        for w in self.input:
            if pre != '#':
                if w[0].isupper():
                    if w in vegs.keys():
                        vegs[w] += pre
                    else:
                        vegs[w] = pre
                pre = '#'
            
            if w.isnumeric():
                pre = int(w)
        return vegs
    
    
    def __getitem__(self, name):
        return self.vegs[name]
    
    def erzeugeIterator(self):
        for e in sorted(self.vegs.items(), key= lambda x: x[1], reverse=True):
            yield e
    
    def __iter__(self):
        return self.erzeugeIterator()
    
    
    
    def keys(self):
        return sorted(self.vegs.keys(), key= lambda x: x[0])
        
    def __len__(self):
        return len(self.vegs)    
    
    
    
if __name__ == '__main__':
    x = Ernte("bauer2.txt" ,"bauer3.txt")
    print(x.keys())
    print(len(x))
    
    for e in x:
        print(e)          
        
    print(x["Moehren"])
    print(3* x["Rueben"] == x["Rueben"], x["Moehren"])
    
    