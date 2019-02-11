'''
Created on 10.02.2019

@author: domee
'''

class UndoList(list):
    
    def __init__(self, *args, **kwargs):
        list.__init__(self, *args, **kwargs)
        self.lis = self
        
    def __add__(self, *args, **kwargs):
        self.lis = self[:]
        return list.__add__(self, *args, **kwargs)

    def __setitem__(self, *args, **kwargs):
        self.lis = self[:]
        return list.__setitem__(self, *args, **kwargs)
    
    def __delitem__(self, *args, **kwargs):
        self.lis = self[:]
        return list.__delitem__(self, *args, **kwargs)
    
    def append(self, *args, **kwargs):
        self.lis = self[:]
        return list.append(self, *args, **kwargs)
    
    def extend(self, *args, **kwargs):
        self.lis = self[:]
        return list.extend(self, *args, **kwargs)

    def insert(self, *args, **kwargs):
        self.lis = self[:]
        return list.insert(self, *args, **kwargs)

    def remove(self, *args, **kwargs):
        self.lis = self[:]
        return list.remove(self, *args, **kwargs)
    
    def undo(self):
        self = self.__init__(self.lis)

if __name__ == '__main__':
    x = UndoList([1,2,3,4,5])
    del x[3]; print(x); x.undo(); print(x)
    x.append(6); print(x); x.undo(); print(x)
    x.extend([6,17,42]); print(x); x.undo(); print(x)
    x.insert(0,0); print(x); x.undo(); print(x)
    x.remove(4); print(x); x.undo(); print(x)
    x[-1] = None; print(x); x.undo(); print(x)
    
    
    
    