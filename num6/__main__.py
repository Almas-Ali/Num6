# !user/bin/env python3

from .packages import *

if __name__ == '__main__':
    menu = '''
Num6 - A Powerful Encrypter And Decrypter Tool
	
1.  For word or line encryption
2.  For word or line decryption

3.  For file encryption enter path
4.  For file decryption enter path

0.  For stop the programme
00. For clearing the screen

© Copyright collected by Md. Almas Ali
'''
    print(menu)

    while 1:
        sta = input('\nChoice : ')

        if sta == '1':
            lop = input('Enter your word : ')
            print(f'Output:\n\n{encrypter(lop)}')
        elif sta == '2':
            lop = input('Enter your word : ')
            print(f'Output:\n\n{decrypter(lop)}')
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
            import os
            if os.name == 'nt':
                os.system('cls')
                print(menu)
            else:
                os.system('clear')
                print(menu)
        else:
            print('Wrong selection try again !')
