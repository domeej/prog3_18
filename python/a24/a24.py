lis = [1,2,3]

def forWhile():
    for e in lis:
        print(e)

    i = 0
    while i < len(lis):
        print(lis[i])
        i += 1

def whileFor():
    m = [5,3,6,8,1]
    i = 0

    while i < len(m):
        z = m[i]
        print(z, "hoch zwei ist", z**2)
        i = i + 1

    for e in m:
        print(e**2)

def devocalize(s):
    voc = 'aeiou'
    lis = ""
    for e in s:
        if e in voc:
            e = ' '
        lis += e
    print(lis)


def dreh(lst):
    if len(lst) == 0:
        return lst
    
    if len(lst) > 0:
        first = lst[0]
        lst = dreh(lst[1:])
    
    return lst + [first]



if __name__ == "__main__":
    print(dreh([1,2,3,4]))