import sys

def test():
    mydict = {'carl':40,
          'alan':2,
          'bob':1,
          'danny':3}

    for key in sorted(mydict.keys()):
        print("%s: %s" % (key, mydict[key]))


def sortDict(dic):
    
    print( {k:v for k,v in sorted(dic.items(), key=lambda x: x[1], reverse=True)} )
    
    
    
def count_chars(f):
    f.seek(0)
    go_to(f,"ACT I")
    dic = {}
    count = 0
    x = f.readline()
    while(x):
        count += 1
        for c in x:
            c = c.lower()
            if not c.isspace():
                if c in dic.keys():
                    dic[c] += 1 
                else:
                    dic[c] = 1
        x = f.readline() 
    res = {k:v for k,v in sorted(dic.items(), key= lambda x: x[1], reverse=True)[:5]}
    print(res, count)


def count_words(f):
    f.seek(0)
    go_to(f,"ACT I")
    count = 0
    dic = {}
    line = f.readline()
    
    with f as fp:
        for line in fp:
            count +=1
            line = line.split()
            for word in line:
                word = word.lower()
                if word in dic:
                    dic[word] += 1
                else:
                    dic[word] = 1
    
    dic = {k:v for k,v in sorted(dic.items(), key=lambda x: x[1], reverse=True)}
    print(dic)
    print(count)

def go_to(f,str):
    line = f.readline()
    
    while(1):
        if str in line:
            print(str, line)
            break
        line = f.readline()
    
    

if __name__ == "__main__":
    FILENAME = sys.argv[1]
    
    f = open(FILENAME, 'r')
    
    count_words(f)
    #count_chars(f)
    
    f.close()
    
    
    
    



