import os
import sys
import argparse
import datetime

# Define args
parser=argparse.ArgumentParser(description='Quicksteg will run steghide, foremost, exiftool, strings and binwalk on an image.')
parser.add_argument('file')
parser.add_argument('-s', '--steghide', action='store_true')
parser.add_argument('-f', '--foremost', action='store_true')
parser.add_argument('-e', '--exiftool', action='store_true')
parser.add_argument('-st', '--strings', action='store_true')
parser.add_argument('-b', '--binwalk', action='store_true')
parser.add_argument('-a', '--all', action='store_true')
# parser.add_argument('-o', '--operations', nargs='*', default='all', const='all', choices=['s', 'f', 'e', 's', 'b', 'all'])
args=parser.parse_args()

file = args.file
now = datetime.datetime.now()
outstr = now.strftime('%Y%m%d%H%M%S')

def steghide():
    os.system('steghide info ' + file + ' >> ' + outstr + '.out')

def foremost():
    os.system('foremost -T ' + file + ' ' + outstr + '.out')

def exiftool():
    os.system('exiftool ' + file + ' >> ' + outstr + '.out')

def strings():
    os.system('strings -f -a ' + file + ' >> ' + outstr + '.out')
    
def binwalk():
    os.system('binwalk -e ' + file + ' >> ' + outstr + '.out')

def main():
    try:
        # Check dependencies
      #  dependencies = ['steghide', 'foremost', 'exiftool', 'strings', 'binwalk']
     #  for i in dependencies:
       #     if not os.system('which ' + i):
       #         print(i + ' is installed')
       #for i in dependencies:
       #     if not os.system('which ' + i):
       #         print(i + ' is installed')
       #     else:
       #          print('You are missing ' + i + '. Please install it using your package manager.')

        file = args.file
        if os.path.exists(file):
            if args.all == True:
                steghide()
                foremost()
                exiftool()
                strings()
                binwalk()
            else:
                if args.steghide == True:
                    steghide()
                elif args.foremost == True:
                    foremost()
                elif i == args.exiftool == True:
                    exiftool()
                elif i == args.strings == True:
                    strings()
                elif i == args.binwalk == True:
                    binwalk()
        else:
            print('The file does not exist')
    except KeyboardInterrupt:
        print(' Exiting...')
        sys.exit(0)
main()