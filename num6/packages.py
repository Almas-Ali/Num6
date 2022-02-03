# Num6

from .charlib import charlib
import re
from collections import defaultdict


# encrypter

def encrypt(string: str, pin: int = 1):
    '''This is encrypt function that takes string data as input and pin as security number. Default pin is 1.'''

    table = string.maketrans(charlib)
    string = string.translate(table)

    # Pin size verification.
    size = len(string) // 2
    if size >= pin:
        pass
    else:
        return '[!] Pin is too large.'

    out = [string[index: index+pin] for index in range(0, len(string), pin)]

    sw = ''
    for i in out:
        sw += i[::-1]

    return sw


# decrypter

def decrypt(string: str, pin: int = 1):
    '''This is decrypt function that takes string data as input and pin as security number. Default pin is 1.'''

    # Pin size verification.
    size = len(string) // 2
    if size >= pin:
        pass
    else:
        return '[!] Pin is too large.'

    out = [string[index: index+pin] for index in range(0, len(string), pin)]

    sw = ''
    for i in out:
        sw += i[::-1]

    com = re.compile(r'\d{6}')
    val = com.findall(sw)
    lib = {v: k for k, v in charlib.items()}

    xlib = defaultdict(lambda: '\n[!] Wrong Character.', lib)

    ret = ''
    for i in val:
        ret += xlib[i]
    val = com.findall(ret)

    if ret == '' or ret.isdigit():
        ret = '[!] Wrong Pin.'

    return ret


def fileEn():
    '''This is file encryption function that works on in CLI mode for now.'''
    fname = input('Enter your file path : ').strip()
    pin = int(input('Enter your pin : ').strip())
    print('Output:\n')
    opo = open(fname).readlines()
    uio = ''
    for abc in opo:
        uio += encrypt(abc, pin)
    return uio


def fileDe():
    '''This is file decryption function that works on in CLI mode for now.'''
    fname = input('Enter your file path : ').strip()
    pin = int(input('Enter your pin : ').strip())
    print('Output:\n')
    opo = open(fname).readlines()
    uio = ''
    for abc in opo:
        uio += decrypt(abc, pin)
    return uio
