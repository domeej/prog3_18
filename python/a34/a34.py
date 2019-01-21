import sys

FILENAME = sys.argv[1]


def decrypt_classic():
    a = "abcdefghijklmnopqrstuvwxyz"
    b = "wgsnqcdvmeyluzoabhrjfkxipt"
    r = ''
    
    with open(FILENAME) as fp:
        line = fp.readline()
        while(line):
            print(line)
            
            for c in line:
                if c in a:
                    for index,e in enumerate(b):                        
                        if c == e:
                            r += a[index]
                else:
                    r += c

            line = fp.readline()
    print (r)   

def decrypt_listcomprehension():
    a = "abcdefghijklmnopqrstuvwxyz"
    b = "wgsnqcdvmeyluzoabhrjfkxipt"
    # wie baue ich das else r+=c da ein?
    with open(FILENAME) as fp:
        print([a[index] for line in fp for c in line for index,e in enumerate(b) if c == e]  )


def decrypt_functional():
    a = "abcdefghijklmnopqrstuvwxyz"
    b = "wgsnqcdvmeyluzoabhrjfkxipt"
    
    pass
    

if __name__ == "__main__":
    decrypt_classic()
    decrypt_listcomprehension()