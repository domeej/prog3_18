import sys
from collections import Counter


FILENAME = sys.argv[1]

def classic():
    classic = {}
    for line in open(FILENAME):
        for c in line:
            c = c.lower()
            if c not in classic.keys() and c.isalpha():
                classic[c] = 1
            elif c.isalpha():
                classic[c] +=1
    print((classic))

# NOCHMAL FRAGEN !
def decrypt():
    commonness = "eniastruhdlcmogkwbzfvpjxyq"
    # dictionary und dann buchstaben zaehlen

    with open(FILENAME, 'r') as content_file:
        dic = {k:v for k, v in Counter(content_file.read().lower()).items() if k.isalpha()}
    
    commonness_encrypted = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    #print(commonness_encrypted)
    print("".join([commonness[i] if x[0] in commonness else c for line in open(FILENAME) for c in line for i,x in enumerate(commonness_encrypted) if x[0] == c]))


def decrypt_2():
    commonness = "eniastruhdlcmogkwbzfvpjxyq"
    # dictionary und dann buchstaben zaehlen
    with open(FILENAME, 'r') as content_file:
        dic = {k:v for k, v in Counter(content_file.read().lower()).items() if k.isalpha()}
    
    commonness_encrypted = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    commonness_encrypted = "".join([e[0] for e in commonness_encrypted])
    print(commonness_encrypted)
    
    #print( "".join( [commonness[i for line in open(FILENAME) for c in line for x,i in enumerate(commonness_encrypted)] ))
    
if __name__ == "__main__":
    #decrypt()
    decrypt_2()
    
    