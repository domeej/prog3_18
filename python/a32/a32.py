FILENAME = "a32-fahrzeiten.txt"

def get_connections(linie):
    connections = []
    with open(FILENAME) as f:
        line = f.readline()
        
        while(line):
            line = line.strip()
            connection = line.split(";")
            
            if connection[0].lower() == linie.lower():
                connections.append(connection)
            
            line = f.readline()
    return connections

def auswertung(fahrt):
    zeit = 0
    haltestellen = []
    for e in fahrt:
        zeit += int(e[3])
        haltestellen.append(e[1])
    haltestellen.append(fahrt[-1][2])
                        
    return (zeit, haltestellen)

def auskunft(linie, start, ziel):
    fahrt = []
    verbindungen = get_connections(linie)
    print(verbindungen)
    
    if start == ziel:
            return 0, [ziel]
    
    while(start != ziel):
        for verbindung in verbindungen:
            if start == verbindung[1]:
                fahrt.append(verbindung)
                start = verbindung[2]
                break
        
    return auswertung(fahrt)   

if __name__ == "__main__":
    print(auskunft("S9", "Kelsterbach", "Niederrad"))