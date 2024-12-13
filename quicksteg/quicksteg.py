import os
import sys

def main():
    try:
        ## Check dependencies
        dependencies = ['steghide', 'foremost', 'exiftool', 'strings', 'binwalk']
        for i in dependencies:
            if not os.system('which ' + i):
                print(i + ' is installed')
            else:
                print('You are missing ' + i + '. Please install it using your package manager.')

        file = input("Enter the location of the file: ")
        if os.path.exists(file):
            os.system('steghide info ' + file + ' >> quicksteg.out')
            os.system('foremost ' + file + ' >> quicksteg.out')
            os.system('exiftool ' + file + ' >> quicksteg.out')
            os.system('strings -a ' + file + ' >> quicksteg.out')
            os.system('binwalk -e ' + file + ' >> quicksteg.out')
        else:
            print('The file does not exist')
    except KeyboardInterrupt:
        print(' Exiting...')
        sys.exit(0)
main()