'''A powerfull encrypter and decrypter tool.

Num6 is a powerfull Encrypter and Decrypter tool for developers or hackers. Depends on user prospective.

This tool has been developed for educational and research based use only. We will not responsible for any type of miss use.

Stay with open source, keep contributing in open source.

Thank you.
Developer Md. Almas Ali
Email: almaspr3@gmail.com
'''

from .packages import *
import argparse
import os

parser = argparse.ArgumentParser(prog='Num6')

__version__ = '0.3.1'

parser.version = __version__


def cli_mode():

    menu = '''\
Num6 - A Powerful Encrypter And Decrypter Tool

1.  For word or line encryption
2.  For word or line decryption

3.  For file encryption enter path
4.  For file decryption enter path

0.  For stop the programme
00. For clearing the screen

© Copyright collected by Md. Almas Ali\
'''
    print(menu)

    while 1:
        sta = input('\nChoice : ')

        if sta == '1':
            lop = input('Enter your word : ')
            print(f'Output:\n\n{encrypt(lop)}')
        elif sta == '2':
            lop = input('Enter your word : ')
            print(f'Output:\n\n{decrypt(lop)}')
        elif sta == '3':
            try:
                En = fileEn()
                print(En)
                try:
                    with open('encoded.txt', 'w') as fff:
                        fff.write(En)
                        print('\nFile encoded.txt saved...')
                except:
                    print('Something went wrong !')
            except:
                print('Wrong path, try again !')
        elif sta == '4':
            try:
                De = fileDe()
                print(De)
                try:
                    with open('decoded.txt', 'w') as fff:
                        fff.write(De)
                        print('\nFile decoded.txt saved...')
                except:
                    print('Something went wrong !')
            except:
                print('Wrong path, try again !')
        elif sta == '0':
            exit('Existing Num6...')
        elif sta == '00':
            if os.name == 'nt':
                os.system('cls')
                print(menu)
            else:
                os.system('clear')
                print(menu)
        else:
            print('Wrong selection try again !')


parser.add_argument('-v', '--version',
                    help='show the version information', action='version')
parser.add_argument('-e', '--encrypt', help='to encrypt data from cli')
parser.add_argument('-d', '--decrypt', help='to decrypt data from cli')
parser.add_argument(
    '-p', '--pin', help='set pin for encrpyt or decrypt data from cli')
parser.add_argument(
    '-c', '--cli', help='to use in interactive cli mode', action='store_true')

args = parser.parse_args()

if args.cli:
    cli_mode()

# print(any(vars(args).values()))

if args.encrypt:
    try:
        print(encrypt(args.encrypt, int(args.pin)))
    except:
        print(encrypt(args.encrypt))

if args.decrypt:
    try:
        print(decrypt(args.decrypt, int(args.pin)))
    except:
        print(decrypt(args.decrypt))

if not any(vars(args).values()):
    print('Num6: error: at least expected one argument')
    parser.print_help()
