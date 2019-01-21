import glob
import os

if __name__ == "__main__":
    print(sorted([[file.split('/')[2], os.path.getsize(file)] for file in glob.glob('/etc/*.conf')], key= lambda entry: entry[1], reverse=True)[:3]   )