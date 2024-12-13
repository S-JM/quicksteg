import os
import sys
import argparse

def main():
    try:
        # Define args
        parser=argparse.ArgumentParser(description='Quicksteg will run steghide, foremost, exiftool, strings and binwalk on an image.')
        parser.add_argument('file')
        args=parser.parse_args()
        # Check dependencies
        dependencies = ['steghide', 'foremost', 'exiftool', 'strings', 'binwalk']
        for i in dependencies:
            if not os.system('which ' + i):
                print(i + ' is installed')
            else:
                print('You are missing ' + i + '. Please install it using your package manager.')

        file = args.file
        if os.path.exists(file):
            os.system('steghide info ' + file + ' >> quicksteg.out')
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