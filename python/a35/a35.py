import sys

FILENAME = sys.argv[1]

def decrypt():
    commonness = "eniastruhdlcmogkwbzfvpjxyq"
    
    print({k for line in open(FILENAME) for k in line})
    


if __name__ == "__main__":
    decrypt()