# Num6

from .charlib import *

# encrypter

def encrypt(string, pin=1):
    '''This is encrypt function that takes string data as input and pin as security number. Default pin is 1.'''
    jo = []
    jk = list(string)
    number = 0
    while number <= pin:
        number += 1
        if number > pin:
            break
        if number == 1:
            pass
        else:
            jk = ''.join(jo)
            jo = []
        for io in jk:
            # Lower Case
            if io == 'a':
                po = io.replace(io, a)
                jo.append(po)
            elif io == 'b':
                po = io.replace(io, b)
                jo.append(po)
            elif io == 'c':
                po = io.replace(io, c)
                jo.append(po)
            elif io == 'd':
                po = io.replace(io, d)
                jo.append(po)
            elif io == 'e':
                po = io.replace(io, e)
                jo.append(po)
            elif io == 'f':
                po = io.replace(io, f)
                jo.append(po)
            elif io == 'g':
                po = io.replace(io, g)
                jo.append(po)
            elif io == 'h':
                po = io.replace(io, h)
                jo.append(po)
            elif io == 'i':
                po = io.replace(io, i)
                jo.append(po)
            elif io == 'j':
                po = io.replace(io, j)
                jo.append(po)
            elif io == 'k':
                po = io.replace(io, k)
                jo.append(po)
            elif io == 'l':
                po = io.replace(io, l)
                jo.append(po)
            elif io == 'm':
                po = io.replace(io, m)
                jo.append(po)
            elif io == 'n':
                po = io.replace(io, n)
                jo.append(po)
            elif io == 'o':
                po = io.replace(io, o)
                jo.append(po)
            elif io == 'p':
                po = io.replace(io, p)
                jo.append(po)
            elif io == 'q':
                po = io.replace(io, q)
                jo.append(po)
            elif io == 'r':
                po = io.replace(io, r)
                jo.append(po)
            elif io == 's':
                po = io.replace(io, s)
                jo.append(po)
            elif io == 't':
                po = io.replace(io, t)
                jo.append(po)
            elif io == 'u':
                po = io.replace(io, u)
                jo.append(po)
            elif io == 'v':
                po = io.replace(io, v)
                jo.append(po)
            elif io == 'w':
                po = io.replace(io, w)
                jo.append(po)
            elif io == 'x':
                po = io.replace(io, x)
                jo.append(po)
            elif io == 'y':
                po = io.replace(io, y)
                jo.append(po)
            elif io == 'z':
                po = io.replace(io, z)
                jo.append(po)
            # Upper Case
            elif io == 'A':
                po = io.replace(io, A)
                jo.append(po)
            elif io == 'B':
                po = io.replace(io, B)
                jo.append(po)
            elif io == 'C':
                po = io.replace(io, C)
                jo.append(po)
            elif io == 'D':
                po = io.replace(io, D)
                jo.append(po)
            elif io == 'E':
                po = io.replace(io, E)
                jo.append(po)
            elif io == 'F':
                po = io.replace(io, F)
                jo.append(po)
            elif io == 'G':
                po = io.replace(io, G)
                jo.append(po)
            elif io == 'H':
                po = io.replace(io, H)
                jo.append(po)
            elif io == 'I':
                po = io.replace(io, I)
                jo.append(po)
            elif io == 'J':
                po = io.replace(io, J)
                jo.append(po)
            elif io == 'K':
                po = io.replace(io, K)
                jo.append(po)
            elif io == 'L':
                po = io.replace(io, L)
                jo.append(po)
            elif io == 'M':
                po = io.replace(io, M)
                jo.append(po)
            elif io == 'N':
                po = io.replace(io, N)
                jo.append(po)
            elif io == 'O':
                po = io.replace(io, O)
                jo.append(po)
            elif io == 'P':
                po = io.replace(io, P)
                jo.append(po)
            elif io == 'Q':
                po = io.replace(io, Q)
                jo.append(po)
            elif io == 'R':
                po = io.replace(io, R)
                jo.append(po)
            elif io == 'S':
                po = io.replace(io, S)
                jo.append(po)
            elif io == 'T':
                po = io.replace(io, T)
                jo.append(po)
            elif io == 'U':
                po = io.replace(io, U)
                jo.append(po)
            elif io == 'V':
                po = io.replace(io, V)
                jo.append(po)
            elif io == 'W':
                po = io.replace(io, W)
                jo.append(po)
            elif io == 'X':
                po = io.replace(io, X)
                jo.append(po)
            elif io == 'Y':
                po = io.replace(io, Y)
                jo.append(po)
            elif io == 'Z':
                po = io.replace(io, Z)
                jo.append(po)
            # Numbers
            elif io == '1':
                po = io.replace(io, one)
                jo.append(po)
            elif io == '2':
                po = io.replace(io, two)
                jo.append(po)
            elif io == '3':
                po = io.replace(io, three)
                jo.append(po)
            elif io == '4':
                po = io.replace(io, four)
                jo.append(po)
            elif io == '5':
                po = io.replace(io, five)
                jo.append(po)
            elif io == '6':
                po = io.replace(io, six)
                jo.append(po)
            elif io == '7':
                po = io.replace(io, seven)
                jo.append(po)
            elif io == '8':
                po = io.replace(io, eight)
                jo.append(po)
            elif io == '9':
                po = io.replace(io, nine)
                jo.append(po)
            elif io == '0':
                po = io.replace(io, zero)
                jo.append(po)
            # Spacial Character
            elif io == '.':
                po = io.replace(io, dot)
                jo.append(po)
            elif io == ' ':
                po = io.replace(io, space)
                jo.append(po)
            elif io == ',':
                po = io.replace(io, comma)
                jo.append(po)
            elif io == '*':
                po = io.replace(io, star)
                jo.append(po)
            elif io == '/':
                po = io.replace(io, fslash)
                jo.append(po)
            elif io == '\\':
                po = io.replace(io, bslash)
                jo.append(po)
            elif io == '@':
                po = io.replace(io, at)
                jo.append(po)
            elif io == '&':
                po = io.replace(io, amp)
                jo.append(po)
            elif io == '%':
                po = io.replace(io, persent)
                jo.append(po)
            elif io == '-':
                po = io.replace(io, dash)
                jo.append(po)
            elif io == '_':
                po = io.replace(io, unders)
                jo.append(po)
            elif io == '!':
                po = io.replace(io, excla)
                jo.append(po)
            elif io == '?':
                po = io.replace(io, question)
                jo.append(po)
            elif io == '\'':
                po = io.replace(io, squort)
                jo.append(po)
            elif io == '\"':
                po = io.replace(io, dquort)
                jo.append(po)
            elif io == '(':
                po = io.replace(io, sbparen)
                jo.append(po)
            elif io == ')':
                po = io.replace(io, cbparen)
                jo.append(po)
            elif io == '[':
                po = io.replace(io, sbsqure)
                jo.append(po)
            elif io == ']':
                po = io.replace(io, cbsqure)
                jo.append(po)
            elif io == '{':
                po = io.replace(io, sbmid)
                jo.append(po)
            elif io == '}':
                po = io.replace(io, cbmid)
                jo.append(po)
            elif io == '+':
                po = io.replace(io, plas)
                jo.append(po)
            elif io == ':':
                po = io.replace(io, colon)
                jo.append(po)
            elif io == '<':
                po = io.replace(io, ssep)
                jo.append(po)
            elif io == '>':
                po = io.replace(io, csep)
                jo.append(po)
            elif io == ';':
                po = io.replace(io, scolon)
                jo.append(po)
            elif io == '×':
                po = io.replace(io, cross)
                jo.append(po)
            elif io == 'π':
                po = io.replace(io, pii)
                jo.append(po)
            elif io == '©':
                po = io.replace(io, copy)
                jo.append(po)
            elif io == '®':
                po = io.replace(io, rr)
                jo.append(po)
            elif io == '√':
                po = io.replace(io, root)
                jo.append(po)
            elif io == '$':
                po = io.replace(io, dollerS)
                jo.append(po)
            elif io == '#':
                po = io.replace(io, hashs)
                jo.append(po)
            elif io == '~':
                po = io.replace(io, aequal)
                jo.append(po)
            elif io == '`':
                po = io.replace(io, hdash)
                jo.append(po)
            elif io == '°':
                po = io.replace(io, degree)
                jo.append(po)
            elif io == '÷':
                po = io.replace(io, vag)
                jo.append(po)
            elif io == '™':
                po = io.replace(io, hTM)
                jo.append(po)
            elif io == '=':
                po = io.replace(io, equal)
                jo.append(po)
            elif io == '≠':
                po = io.replace(io, nequal)
                jo.append(po)
            elif io == '≈':
                po = io.replace(io, alequal)
                jo.append(po)
            elif io == '♪':
                po = io.replace(io, song)
                jo.append(po)
            elif io == '|':
                po = io.replace(io, ll)
                jo.append(po)
            elif io == '^':
                po = io.replace(io, powerof)
                jo.append(po)
            elif io == '£':
                po = io.replace(io, dS)
                jo.append(po)
            elif io == '\t':
                po = io.replace(io, tab)
                jo.append(po)
            elif io == '\n':
                po = io.replace(io, newL)
                jo.append(po)
            else:
                print(f'Unknown Character found \'{io}\' !')

    return ''.join(jo)


# decrypter

def decrypt(string, pin=1):
    '''This is decrypt function that takes string data as input and pin as security number. Default pin is 1.'''
    yu = []
    ui = ''
    number = 0
    while number <= pin:
        number += 1
        if number > pin:
            break
        if number == 1:
            pass
        else:
            string = ''.join(yu)
            yu = []

        for kl in string:
            ui += kl
            if len(ui) == 6:
                #  Spacial Character
                if ui == space:
                    pp = ui.replace(ui, ' ')
                    yu.append(pp)
                    ui = ''
                elif ui == dot:
                    pp = ui.replace(ui, '.')
                    yu.append(pp)
                    ui = ''
                elif ui == star:
                    pp = ui.replace(ui, '*')
                    yu.append(pp)
                    ui = ''
                elif ui == comma:
                    pp = ui.replace(ui, ',')
                    yu.append(pp)
                    ui = ''
                elif ui == fslash:
                    pp = ui.replace(ui, '/')
                    yu.append(pp)
                    ui = ''
                elif ui == bslash:
                    pp = ui.replace(ui, '\\')
                    yu.append(pp)
                    ui = ''
                elif ui == at:
                    pp = ui.replace(ui, '@')
                    yu.append(pp)
                    ui = ''
                elif ui == amp:
                    pp = ui.replace(ui, '&')
                    yu.append(pp)
                    ui = ''
                elif ui == persent:
                    pp = ui.replace(ui, '%')
                    yu.append(pp)
                    ui = ''
                elif ui == dash:
                    pp = ui.replace(ui, '-')
                    yu.append(pp)
                    ui = ''
                elif ui == unders:
                    pp = ui.replace(ui, '_')
                    yu.append(pp)
                    ui = ''
                elif ui == excla:
                    pp = ui.replace(ui, '!')
                    yu.append(pp)
                    ui = ''
                elif ui == question:
                    pp = ui.replace(ui, '?')
                    yu.append(pp)
                    ui = ''
                elif ui == squort:
                    pp = ui.replace(ui, '\'')
                    yu.append(pp)
                    ui = ''
                elif ui == dquort:
                    pp = ui.replace(ui, '\"')
                    yu.append(pp)
                    ui = ''
                elif ui == sbparen:
                    pp = ui.replace(ui, '(')
                    yu.append(pp)
                    ui = ''
                elif ui == cbparen:
                    pp = ui.replace(ui, ')')
                    yu.append(pp)
                    ui = ''
                elif ui == sbsqure:
                    pp = ui.replace(ui, '[')
                    yu.append(pp)
                    ui = ''
                elif ui == cbsqure:
                    pp = ui.replace(ui, ']')
                    yu.append(pp)
                    ui = ''
                elif ui == sbmid:
                    pp = ui.replace(ui, '{')
                    yu.append(pp)
                    ui = ''
                elif ui == cbmid:
                    pp = ui.replace(ui, '}')
                    yu.append(pp)
                    ui = ''
                elif ui == plas:
                    pp = ui.replace(ui, '+')
                    yu.append(pp)
                    ui = ''
                elif ui == colon:
                    pp = ui.replace(ui, ':')
                    yu.append(pp)
                    ui = ''
                elif ui == ssep:
                    pp = ui.replace(ui, '<')
                    yu.append(pp)
                    ui = ''
                elif ui == csep:
                    pp = ui.replace(ui, '>')
                    yu.append(pp)
                    ui = ''
                elif ui == scolon:
                    pp = ui.replace(ui, ';')
                    yu.append(pp)
                    ui = ''
                elif ui == cross:
                    pp = ui.replace(ui, '×')
                    yu.append(pp)
                    ui = ''
                elif ui == pii:
                    pp = ui.replace(ui, 'π')
                    yu.append(pp)
                    ui = ''
                elif ui == copy:
                    pp = ui.replace(ui, '©')
                    yu.append(pp)
                    ui = ''
                elif ui == rr:
                    pp = ui.replace(ui, '®')
                    yu.append(pp)
                    ui = ''
                elif ui == root:
                    pp = ui.replace(ui, '√')
                    yu.append(pp)
                    ui = ''
                elif ui == dollerS:
                    pp = ui.replace(ui, '$')
                    yu.append(pp)
                    ui = ''
                elif ui == hashs:
                    pp = ui.replace(ui, '#')
                    yu.append(pp)
                    ui = ''
                elif ui == aequal:
                    pp = ui.replace(ui, '~')
                    yu.append(pp)
                    ui = ''
                elif ui == hdash:
                    pp = ui.replace(ui, '`')
                    yu.append(pp)
                    ui = ''
                elif ui == degree:
                    pp = ui.replace(ui, '°')
                    yu.append(pp)
                    ui = ''
                elif ui == vag:
                    pp = ui.replace(ui, '÷')
                    yu.append(pp)
                    ui = ''
                elif ui == hTM:
                    pp = ui.replace(ui, '™')
                    yu.append(pp)
                    ui = ''
                elif ui == equal:
                    pp = ui.replace(ui, '=')
                    yu.append(pp)
                    ui = ''
                elif ui == nequal:
                    pp = ui.replace(ui, '≠')
                    yu.append(pp)
                    ui = ''
                elif ui == alequal:
                    pp = ui.replace(ui, '≈')
                    yu.append(pp)
                    ui = ''
                elif ui == song:
                    pp = ui.replace(ui, '♪')
                    yu.append(pp)
                    ui = ''
                elif ui == ll:
                    pp = ui.replace(ui, '|')
                    yu.append(pp)
                    ui = ''
                elif ui == powerof:
                    pp = ui.replace(ui, '^')
                    yu.append(pp)
                    ui = ''
                elif ui == dS:
                    pp = ui.replace(ui, '£')
                    yu.append(pp)
                    ui = ''
                elif ui == tab:
                    pp = ui.replace(ui, '\t')
                    yu.append(pp)
                    ui = ''
                elif ui == newL:
                    pp = ui.replace(ui, '\n')
                    yu.append(pp)
                    ui = ''
                # Numbers
                elif ui == one:
                    pp = ui.replace(ui, '1')
                    yu.append(pp)
                    ui = ''
                elif ui == two:
                    pp = ui.replace(ui, '2')
                    yu.append(pp)
                    ui = ''
                elif ui == three:
                    pp = ui.replace(ui, '3')
                    yu.append(pp)
                    ui = ''
                elif ui == four:
                    pp = ui.replace(ui, '4')
                    yu.append(pp)
                    ui = ''
                elif ui == five:
                    pp = ui.replace(ui, '5')
                    yu.append(pp)
                    ui = ''
                elif ui == six:
                    pp = ui.replace(ui, '6')
                    yu.append(pp)
                    ui = ''
                elif ui == seven:
                    pp = ui.replace(ui, '7')
                    yu.append(pp)
                    ui = ''
                elif ui == eight:
                    pp = ui.replace(ui, '8')
                    yu.append(pp)
                    ui = ''
                elif ui == nine:
                    pp = ui.replace(ui, '9')
                    yu.append(pp)
                    ui = ''
                elif ui == zero:
                    pp = ui.replace(ui, '0')
                    yu.append(pp)
                    ui = ''
                # Lower Case
                elif ui == a:
                    pp = ui.replace(ui, 'a')
                    yu.append(pp)
                    ui = ''
                elif ui == b:
                    pp = ui.replace(ui, 'b')
                    yu.append(pp)
                    ui = ''
                elif ui == c:
                    pp = ui.replace(ui, 'c')
                    yu.append(pp)
                    ui = ''
                elif ui == d:
                    pp = ui.replace(ui, 'd')
                    yu.append(pp)
                    ui = ''
                elif ui == e:
                    pp = ui.replace(ui, 'e')
                    yu.append(pp)
                    ui = ''
                elif ui == f:
                    pp = ui.replace(ui, 'f')
                    yu.append(pp)
                    ui = ''
                elif ui == g:
                    pp = ui.replace(ui, 'g')
                    yu.append(pp)
                    ui = ''
                elif ui == h:
                    pp = ui.replace(ui, 'h')
                    yu.append(pp)
                    ui = ''
                elif ui == i:
                    pp = ui.replace(ui, 'i')
                    yu.append(pp)
                    ui = ''
                elif ui == j:
                    pp = ui.replace(ui, 'j')
                    yu.append(pp)
                    ui = ''
                elif ui == k:
                    pp = ui.replace(ui, 'k')
                    yu.append(pp)
                    ui = ''
                elif ui == l:
                    pp = ui.replace(ui, 'l')
                    yu.append(pp)
                    ui = ''
                elif ui == m:
                    pp = ui.replace(ui, 'm')
                    yu.append(pp)
                    ui = ''
                elif ui == n:
                    pp = ui.replace(ui, 'n')
                    yu.append(pp)
                    ui = ''
                elif ui == o:
                    pp = ui.replace(ui, 'o')
                    yu.append(pp)
                    ui = ''
                elif ui == p:
                    pp = ui.replace(ui, 'p')
                    yu.append(pp)
                    ui = ''
                elif ui == q:
                    pp = ui.replace(ui, 'q')
                    yu.append(pp)
                    ui = ''
                elif ui == r:
                    pp = ui.replace(ui, 'r')
                    yu.append(pp)
                    ui = ''
                elif ui == s:
                    pp = ui.replace(ui, 's')
                    yu.append(pp)
                    ui = ''
                elif ui == t:
                    pp = ui.replace(ui, 't')
                    yu.append(pp)
                    ui = ''
                elif ui == u:
                    pp = ui.replace(ui, 'u')
                    yu.append(pp)
                    ui = ''
                elif ui == v:
                    pp = ui.replace(ui, 'v')
                    yu.append(pp)
                    ui = ''
                elif ui == w:
                    pp = ui.replace(ui, 'w')
                    yu.append(pp)
                    ui = ''
                elif ui == x:
                    pp = ui.replace(ui, 'x')
                    yu.append(pp)
                    ui = ''
                elif ui == y:
                    pp = ui.replace(ui, 'y')
                    yu.append(pp)
                    ui = ''
                elif ui == z:
                    pp = ui.replace(ui, 'z')
                    yu.append(pp)
                    ui = ''
                # Upper Case
                elif ui == A:
                    pp = ui.replace(ui, 'A')
                    yu.append(pp)
                    ui = ''
                elif ui == B:
                    pp = ui.replace(ui, 'B')
                    yu.append(pp)
                    ui = ''
                elif ui == C:
                    pp = ui.replace(ui, 'C')
                    yu.append(pp)
                    ui = ''
                elif ui == D:
                    pp = ui.replace(ui, 'D')
                    yu.append(pp)
                    ui = ''
                elif ui == E:
                    pp = ui.replace(ui, 'E')
                    yu.append(pp)
                    ui = ''
                elif ui == F:
                    pp = ui.replace(ui, 'F')
                    yu.append(pp)
                    ui = ''
                elif ui == G:
                    pp = ui.replace(ui, 'G')
                    yu.append(pp)
                    ui = ''
                elif ui == H:
                    pp = ui.replace(ui, 'H')
                    yu.append(pp)
                    ui = ''
                elif ui == I:
                    pp = ui.replace(ui, 'I')
                    yu.append(pp)
                    ui = ''
                elif ui == J:
                    pp = ui.replace(ui, 'J')
                    yu.append(pp)
                    ui = ''
                elif ui == K:
                    pp = ui.replace(ui, 'K')
                    yu.append(pp)
                    ui = ''
                elif ui == L:
                    pp = ui.replace(ui, 'L')
                    yu.append(pp)
                    ui = ''
                elif ui == M:
                    pp = ui.replace(ui, 'M')
                    yu.append(pp)
                    ui = ''
                elif ui == N:
                    pp = ui.replace(ui, 'N')
                    yu.append(pp)
                    ui = ''
                elif ui == O:
                    pp = ui.replace(ui, 'O')
                    yu.append(pp)
                    ui = ''
                elif ui == P:
                    pp = ui.replace(ui, 'P')
                    yu.append(pp)
                    ui = ''
                elif ui == Q:
                    pp = ui.replace(ui, 'Q')
                    yu.append(pp)
                    ui = ''
                elif ui == R:
                    pp = ui.replace(ui, 'R')
                    yu.append(pp)
                    ui = ''
                elif ui == S:
                    pp = ui.replace(ui, 'S')
                    yu.append(pp)
                    ui = ''
                elif ui == T:
                    pp = ui.replace(ui, 'T')
                    yu.append(pp)
                    ui = ''
                elif ui == U:
                    pp = ui.replace(ui, 'U')
                    yu.append(pp)
                    ui = ''
                elif ui == V:
                    pp = ui.replace(ui, 'V')
                    yu.append(pp)
                    ui = ''
                elif ui == W:
                    pp = ui.replace(ui, 'W')
                    yu.append(pp)
                    ui = ''
                elif ui == X:
                    pp = ui.replace(ui, 'X')
                    yu.append(pp)
                    ui = ''
                elif ui == Y:
                    pp = ui.replace(ui, 'Y')
                    yu.append(pp)
                    ui = ''
                elif ui == Z:
                    pp = ui.replace(ui, 'Z')
                    yu.append(pp)
                    ui = ''
                else:
                    print(f'Unknown Character found \'{ui}\' !')
                    ui = ''

    return ''.join(yu)


def fileEn():
    '''This is file encryption function that works on in CLI mode for now.'''
    fname = input('Enter your file path : ').strip()
    print('Output:\n')
    opo = open(fname).readlines()
    uio = ''
    for abc in opo:
        uio += encrypt(abc)
    return uio


def fileDe():
    '''This is file decryption function that works on in CLI mode for now.'''
    fname = input('Enter your file path : ').strip()
    print('Output:\n')
    opo = open(fname).readlines()
    uio = ''
    for abc in opo:
        uio += decrypt(abc)
    return uio
