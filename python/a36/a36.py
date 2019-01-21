FILENAME = "a36-bonz.txt"

def do():
    #eine aufsteigend sortiere Liste der Wohnorte aller Männer
    print( sorted([x[4].rstrip() for x in [e.split(';') for e in [line for line in open(FILENAME)]] if x[0] == 'Herr']) )
    print( sorted([entry[4].rstrip() for line in open(FILENAME) for entry in [line.split(';')] if entry[0] == 'Herr' ]) )
        
    #die Summe der Gehälter aller Frauen
    print(  sum([int(entry[3]) for line in open(FILENAME) for entry in [line.split(';')] if entry[0] == 'Frau'])    )
    print( sorted([x[3].rstrip() for x in [e.split(';') for e in [line for line in open(FILENAME)]] if x[0] == 'Frau']) )
    
    #den  Wohnort  der  Person,  die  unter  allen,  deren  Vorname  mit  ’J’  beginnt,  am  meisten  verdient  (bzw.bekommt)
    print( max([[entry[4].rstrip(), int(entry[3])] for line in open(FILENAME) for entry in [line.split(';')] if entry[2].startswith('J')] ,key=lambda item:item[1])[1] )
    
    #schmähungen für gehalt größer 100000
    print([entry[0] +' '+ entry[1] + " bekommt mehr als "+ ("er verdient" if entry[0] == "Herr" else "sie verdient!") for line in open(FILENAME) for entry in [line.split(';')] if int(entry[3]) > 100000]     )
    
    
if __name__ == "__main__":
    do()