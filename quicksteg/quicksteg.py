import os
import sys
import argparse
import datetime

# Define args
parser=argparse.ArgumentParser(description='Quicksteg will run steghide, foremost, exiftool, strings and binwalk on an image.')
parser.add_argument('file')
args=parser.parse_args()

file = args.file
now = datetime.datetime.now()
outstr = now.strftime('%Y%m%d%H%M%S')

def steghide():
    os.system('steghide info ' + file + ' >> ' + outstr + '_' + file + '.out')

def foremost():
    os.system('foremost -T ' + file + ' ' + outstr + '_' + file + '.out')

def exiftool():
    os.system('exiftool ' + file + ' >> ' + outstr + '_' + file + '.out')

def strings():
    os.system('strings -f -a ' + file + ' >> ' + outstr + '_' + file + '.out')
    
def main():
    try:
        # Check dependencies
        dependencies = ['steghide', 'foremost', 'exiftool', 'strings', 'binwalk']
        for i in dependencies:
            if not os.system('which ' + i):
                print(i + ' is installed')
            else:
                print('You are missing ' + i + '. Please install it using your package manager.')

        file = args.file
        if os.path.exists(file):
            os.system('foremost -T ' + file + ' >> quicksteg.out')
            os.system('exiftool ' + file + ' >> quicksteg.out')
            os.system('strings -f -a ' + file + ' >> quicksteg.out')
            os.system('binwalk -e ' + file + ' >> quicksteg.out')
        else:
            print('The file does not exist')
    except KeyboardInterrupt:
        print(' Exiting...')
        sys.exit(0)
main()