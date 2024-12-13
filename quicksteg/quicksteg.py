import os
import sys

## Check dependencies
#dependencies = ['steghide', 'foremost', 'exiftool', 'strings', 'binwalk']
#for i in dependencies:
#    if not os.system('which ' + i):
#        print(i + ' is installed')
#    else:
#        print('Installing' + i)
#        os.system('sudo apt-get install ' + i)

def main():
    try:
        file = input("Enter the location of the file: ")
        if os.path.exists(file):
            os.system('steghide info ' + file + ' > steghide.txt')
            os.system('foremost ' + file + ' > foremost.txt')
            os.system('exiftool ' + file + ' > exiftool.txt')
            os.system('strings -a ' + file + ' > strings.txt')
            os.system('binwalk -e ' + file + ' > binwalk.txt')
        else:
            print('The file does not exist')
    except KeyboardInterrupt:
        print('Exiting...')
        sys.exit(0)
main()