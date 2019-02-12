'''
Created on 12.02.2019

@author: dkoeh001
'''

def process(lines, split=";", key=0, del_key=False):
    dic = {}
    lines = lines[1:]
   
    for line in lines:
        line = line.split(split)
        dkey = line[key]


        if del_key:
            for e in line:
                if e == dkey:
                    line.remove(e)
            dic[dkey] = line
        else:
            dic[dkey] = line
    
    return dic

if __name__ == '__main__':
    lines = []
    
    
    for line in open("data.txt"):
        line = line.strip()
        lines.append(line)

        #lines.extend(line)

    print(process(lines, split=';', key=0, del_key=False))