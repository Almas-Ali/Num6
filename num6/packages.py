# Num6

from .charlib import *

# encrypter

def encrypt(string, pin=1):
    '''This is encrypt function that takes string data as input and pin as security number. Default pin is 1.'''
    _jo = []
    jk = list(string)
    number = 0
    while number <= pin:
        number += 1
        if number > pin:
            break
        if number == 1:
            pass
        else:
            jk = ''.join(_jo)
            _jo = []
        for _io in jk:
            # Lower Case
            if _io == 'a':
                po = _io.replace(_io, _a)
                _jo.append(po)
            elif _io == 'b':
                po = _io.replace(_io, _b)
                _jo.append(po)
            elif _io == 'c':
                po = _io.replace(_io, _c)
                _jo.append(po)
            elif _io == 'd':
                po = _io.replace(_io, _d)
                _jo.append(po)
            elif _io == 'e':
                po = _io.replace(_io, _e)
                _jo.append(po)
            elif _io == 'f':
                po = _io.replace(_io, _f)
                _jo.append(po)
            elif _io == 'g':
                po = _io.replace(_io, _g)
                _jo.append(po)
            elif _io == 'h':
                po = _io.replace(_io, _h)
                _jo.append(po)
            elif _io == 'i':
                po = _io.replace(_io, _i)
                _jo.append(po)
            elif _io == 'j':
                po = _io.replace(_io, _j)
                _jo.append(po)
            elif _io == 'k':
                po = _io.replace(_io, _k)
                _jo.append(po)
            elif _io == 'l':
                po = _io.replace(_io, _l)
                _jo.append(po)
            elif _io == 'm':
                po = _io.replace(_io, _m)
                _jo.append(po)
            elif _io == 'n':
                po = _io.replace(_io, _n)
                _jo.append(po)
            elif _io == 'o':
                po = _io.replace(_io, _o)
                _jo.append(po)
            elif _io == 'p':
                po = _io.replace(_io, _p)
                _jo.append(po)
            elif _io == 'q':
                po = _io.replace(_io, _q)
                _jo.append(po)
            elif _io == 'r':
                po = _io.replace(_io, _r)
                _jo.append(po)
            elif _io == 's':
                po = _io.replace(_io, _s)
                _jo.append(po)
            elif _io == 't':
                po = _io.replace(_io, _t)
                _jo.append(po)
            elif _io == 'u':
                po = _io.replace(_io, _u)
                _jo.append(po)
            elif _io == 'v':
                po = _io.replace(_io, _v)
                _jo.append(po)
            elif _io == 'w':
                po = _io.replace(_io, _w)
                _jo.append(po)
            elif _io == 'x':
                po = _io.replace(_io, _x)
                _jo.append(po)
            elif _io == 'y':
                po = _io.replace(_io, _y)
                _jo.append(po)
            elif _io == 'z':
                po = _io.replace(_io, _z)
                _jo.append(po)
            # Upper Case
            elif _io == 'A':
                po = _io.replace(_io, _A)
                _jo.append(po)
            elif _io == 'B':
                po = _io.replace(_io, _B)
                _jo.append(po)
            elif _io == 'C':
                po = _io.replace(_io, _C)
                _jo.append(po)
            elif _io == 'D':
                po = _io.replace(_io, _D)
                _jo.append(po)
            elif _io == 'E':
                po = _io.replace(_io, _E)
                _jo.append(po)
            elif _io == 'F':
                po = _io.replace(_io, _F)
                _jo.append(po)
            elif _io == 'G':
                po = _io.replace(_io, _G)
                _jo.append(po)
            elif _io == 'H':
                po = _io.replace(_io, _H)
                _jo.append(po)
            elif _io == 'I':
                po = _io.replace(_io, _I)
                _jo.append(po)
            elif _io == 'J':
                po = _io.replace(_io, _J)
                _jo.append(po)
            elif _io == 'K':
                po = _io.replace(_io, _K)
                _jo.append(po)
            elif _io == 'L':
                po = _io.replace(_io, _L)
                _jo.append(po)
            elif _io == 'M':
                po = _io.replace(_io, _M)
                _jo.append(po)
            elif _io == 'N':
                po = _io.replace(_io, _N)
                _jo.append(po)
            elif _io == 'O':
                po = _io.replace(_io, _O)
                _jo.append(po)
            elif _io == 'P':
                po = _io.replace(_io, _P)
                _jo.append(po)
            elif _io == 'Q':
                po = _io.replace(_io, _Q)
                _jo.append(po)
            elif _io == 'R':
                po = _io.replace(_io, _R)
                _jo.append(po)
            elif _io == 'S':
                po = _io.replace(_io, _S)
                _jo.append(po)
            elif _io == 'T':
                po = _io.replace(_io, _T)
                _jo.append(po)
            elif _io == 'U':
                po = _io.replace(_io, _U)
                _jo.append(po)
            elif _io == 'V':
                po = _io.replace(_io, _V)
                _jo.append(po)
            elif _io == 'W':
                po = _io.replace(_io, _W)
                _jo.append(po)
            elif _io == 'X':
                po = _io.replace(_io, _X)
                _jo.append(po)
            elif _io == 'Y':
                po = _io.replace(_io, _Y)
                _jo.append(po)
            elif _io == 'Z':
                po = _io.replace(_io, _Z)
                _jo.append(po)
            # Numbers
            elif _io == '1':
                po = _io.replace(_io, _one)
                _jo.append(po)
            elif _io == '2':
                po = _io.replace(_io, _two)
                _jo.append(po)
            elif _io == '3':
                po = _io.replace(_io, _three)
                _jo.append(po)
            elif _io == '4':
                po = _io.replace(_io, _four)
                _jo.append(po)
            elif _io == '5':
                po = _io.replace(_io, _five)
                _jo.append(po)
            elif _io == '6':
                po = _io.replace(_io, _six)
                _jo.append(po)
            elif _io == '7':
                po = _io.replace(_io, _seven)
                _jo.append(po)
            elif _io == '8':
                po = _io.replace(_io, _eight)
                _jo.append(po)
            elif _io == '9':
                po = _io.replace(_io, _nine)
                _jo.append(po)
            elif _io == '0':
                po = _io.replace(_io, _zero)
                _jo.append(po)
            # Spacial Character
            elif _io == '.':
                po = _io.replace(_io, _dot)
                _jo.append(po)
            elif _io == ' ':
                po = _io.replace(_io, _space)
                _jo.append(po)
            elif _io == ',':
                po = _io.replace(_io, _comma)
                _jo.append(po)
            elif _io == '*':
                po = _io.replace(_io, _star)
                _jo.append(po)
            elif _io == '/':
                po = _io.replace(_io, _fslash)
                _jo.append(po)
            elif _io == '\\':
                po = _io.replace(_io, _bslash)
                _jo.append(po)
            elif _io == '@':
                po = _io.replace(_io, _at)
                _jo.append(po)
            elif _io == '&':
                po = _io.replace(_io, _amp)
                _jo.append(po)
            elif _io == '%':
                po = _io.replace(_io, _persent)
                _jo.append(po)
            elif _io == '-':
                po = _io.replace(_io, _dash)
                _jo.append(po)
            elif _io == '_':
                po = _io.replace(_io, _unders)
                _jo.append(po)
            elif _io == '!':
                po = _io.replace(_io, _excla)
                _jo.append(po)
            elif _io == '?':
                po = _io.replace(_io, _question)
                _jo.append(po)
            elif _io == '\'':
                po = _io.replace(_io, _squort)
                _jo.append(po)
            elif _io == '\"':
                po = _io.replace(_io, _dquort)
                _jo.append(po)
            elif _io == '(':
                po = _io.replace(_io, _sbparen)
                _jo.append(po)
            elif _io == ')':
                po = _io.replace(_io, _cbparen)
                _jo.append(po)
            elif _io == '[':
                po = _io.replace(_io, _sbsqure)
                _jo.append(po)
            elif _io == ']':
                po = _io.replace(_io, _cbsqure)
                _jo.append(po)
            elif _io == '{':
                po = _io.replace(_io, _sbmid)
                _jo.append(po)
            elif _io == '}':
                po = _io.replace(_io, _cbmid)
                _jo.append(po)
            elif _io == '+':
                po = _io.replace(_io, _plas)
                _jo.append(po)
            elif _io == ':':
                po = _io.replace(_io, _colon)
                _jo.append(po)
            elif _io == '<':
                po = _io.replace(_io, _ssep)
                _jo.append(po)
            elif _io == '>':
                po = _io.replace(_io, _csep)
                _jo.append(po)
            elif _io == ';':
                po = _io.replace(_io, _scolon)
                _jo.append(po)
            elif _io == '×':
                po = _io.replace(_io, _cross)
                _jo.append(po)
            elif _io == 'π':
                po = _io.replace(_io, _pii)
                _jo.append(po)
            elif _io == '©':
                po = _io.replace(_io, _copy)
                _jo.append(po)
            elif _io == '®':
                po = _io.replace(_io, _rr)
                _jo.append(po)
            elif _io == '√':
                po = _io.replace(_io, _root)
                _jo.append(po)
            elif _io == '$':
                po = _io.replace(_io, _dollerS)
                _jo.append(po)
            elif _io == '#':
                po = _io.replace(_io, _hashs)
                _jo.append(po)
            elif _io == '~':
                po = _io.replace(_io, _aequal)
                _jo.append(po)
            elif _io == '`':
                po = _io.replace(_io, _hdash)
                _jo.append(po)
            elif _io == '°':
                po = _io.replace(_io, _degree)
                _jo.append(po)
            elif _io == '÷':
                po = _io.replace(_io, _vag)
                _jo.append(po)
            elif _io == '™':
                po = _io.replace(_io, _hTM)
                _jo.append(po)
            elif _io == '=':
                po = _io.replace(_io, _equal)
                _jo.append(po)
            elif _io == '≠':
                po = _io.replace(_io, _nequal)
                _jo.append(po)
            elif _io == '≈':
                po = _io.replace(_io, _alequal)
                _jo.append(po)
            elif _io == '♪':
                po = _io.replace(_io, _song)
                _jo.append(po)
            elif _io == '|':
                po = _io.replace(_io, _ll)
                _jo.append(po)
            elif _io == '^':
                po = _io.replace(_io, _powerof)
                _jo.append(po)
            elif _io == '£':
                po = _io.replace(_io, _dS)
                _jo.append(po)
            elif _io == '\t':
                po = _io.replace(_io, _tab)
                _jo.append(po)
            elif _io == '\n':
                po = _io.replace(_io, _newL)
                _jo.append(po)
            else:
                print(f'Unknown Character found \'{_io}\' !')

    return ''.join(_jo)


# decrypter

def decrypt(string, pin=1):
    '''This is decrypt function that takes string data as input and pin as security number. Default pin is 1.'''
    _yu = []
    _ui = ''
    number = 0
    while number <= pin:
        number += 1
        if number > pin:
            break
        if number == 1:
            pass
        else:
            string = ''.join(_yu)
            _yu = []

        for kl in string:
            _ui += kl
            if len(_ui) == 6:
                #  Spacial Character
                if _ui == _space:
                    pp = _ui.replace(_ui, ' ')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _dot:
                    pp = _ui.replace(_ui, '.')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _star:
                    pp = _ui.replace(_ui, '*')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _comma:
                    pp = _ui.replace(_ui, ',')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _fslash:
                    pp = _ui.replace(_ui, '/')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _bslash:
                    pp = _ui.replace(_ui, '\\')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _at:
                    pp = _ui.replace(_ui, '@')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _amp:
                    pp = _ui.replace(_ui, '&')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _persent:
                    pp = _ui.replace(_ui, '%')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _dash:
                    pp = _ui.replace(_ui, '-')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _unders:
                    pp = _ui.replace(_ui, '_')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _excla:
                    pp = _ui.replace(_ui, '!')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _question:
                    pp = _ui.replace(_ui, '?')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _squort:
                    pp = _ui.replace(_ui, '\'')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _dquort:
                    pp = _ui.replace(_ui, '\"')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _sbparen:
                    pp = _ui.replace(_ui, '(')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _cbparen:
                    pp = _ui.replace(_ui, ')')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _sbsqure:
                    pp = _ui.replace(_ui, '[')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _cbsqure:
                    pp = _ui.replace(_ui, ']')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _sbmid:
                    pp = _ui.replace(_ui, '{')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _cbmid:
                    pp = _ui.replace(_ui, '}')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _plas:
                    pp = _ui.replace(_ui, '+')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _colon:
                    pp = _ui.replace(_ui, ':')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _ssep:
                    pp = _ui.replace(_ui, '<')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _csep:
                    pp = _ui.replace(_ui, '>')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _scolon:
                    pp = _ui.replace(_ui, ';')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _cross:
                    pp = _ui.replace(_ui, '×')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _pii:
                    pp = _ui.replace(_ui, 'π')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _copy:
                    pp = _ui.replace(_ui, '©')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _rr:
                    pp = _ui.replace(_ui, '®')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _root:
                    pp = _ui.replace(_ui, '√')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _dollerS:
                    pp = _ui.replace(_ui, '$')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _hashs:
                    pp = _ui.replace(_ui, '#')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _aequal:
                    pp = _ui.replace(_ui, '~')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _hdash:
                    pp = _ui.replace(_ui, '`')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _degree:
                    pp = _ui.replace(_ui, '°')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _vag:
                    pp = _ui.replace(_ui, '÷')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _hTM:
                    pp = _ui.replace(_ui, '™')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _equal:
                    pp = _ui.replace(_ui, '=')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _nequal:
                    pp = _ui.replace(_ui, '≠')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _alequal:
                    pp = _ui.replace(_ui, '≈')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _song:
                    pp = _ui.replace(_ui, '♪')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _ll:
                    pp = _ui.replace(_ui, '|')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _powerof:
                    pp = _ui.replace(_ui, '^')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _dS:
                    pp = _ui.replace(_ui, '£')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _tab:
                    pp = _ui.replace(_ui, '\t')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _newL:
                    pp = _ui.replace(_ui, '\n')
                    _yu.append(pp)
                    _ui = ''
                # Numbers
                elif _ui == _one:
                    pp = _ui.replace(_ui, '1')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _two:
                    pp = _ui.replace(_ui, '2')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _three:
                    pp = _ui.replace(_ui, '3')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _four:
                    pp = _ui.replace(_ui, '4')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _five:
                    pp = _ui.replace(_ui, '5')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _six:
                    pp = _ui.replace(_ui, '6')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _seven:
                    pp = _ui.replace(_ui, '7')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _eight:
                    pp = _ui.replace(_ui, '8')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _nine:
                    pp = _ui.replace(_ui, '9')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _zero:
                    pp = _ui.replace(_ui, '0')
                    _yu.append(pp)
                    _ui = ''
                # Lower Case
                elif _ui == _a:
                    pp = _ui.replace(_ui, 'a')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _b:
                    pp = _ui.replace(_ui, 'b')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _c:
                    pp = _ui.replace(_ui, 'c')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _d:
                    pp = _ui.replace(_ui, 'd')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _e:
                    pp = _ui.replace(_ui, 'e')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _f:
                    pp = _ui.replace(_ui, 'f')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _g:
                    pp = _ui.replace(_ui, 'g')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _h:
                    pp = _ui.replace(_ui, 'h')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _i:
                    pp = _ui.replace(_ui, 'i')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _j:
                    pp = _ui.replace(_ui, 'j')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _k:
                    pp = _ui.replace(_ui, 'k')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _l:
                    pp = _ui.replace(_ui, 'l')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _m:
                    pp = _ui.replace(_ui, 'm')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _n:
                    pp = _ui.replace(_ui, 'n')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _o:
                    pp = _ui.replace(_ui, 'o')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _p:
                    pp = _ui.replace(_ui, 'p')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _q:
                    pp = _ui.replace(_ui, 'q')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _r:
                    pp = _ui.replace(_ui, 'r')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _s:
                    pp = _ui.replace(_ui, 's')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _t:
                    pp = _ui.replace(_ui, 't')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _u:
                    pp = _ui.replace(_ui, 'u')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _v:
                    pp = _ui.replace(_ui, 'v')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _w:
                    pp = _ui.replace(_ui, 'w')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _x:
                    pp = _ui.replace(_ui, 'x')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _y:
                    pp = _ui.replace(_ui, 'y')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _z:
                    pp = _ui.replace(_ui, 'z')
                    _yu.append(pp)
                    _ui = ''
                # Upper Case
                elif _ui == _A:
                    pp = _ui.replace(_ui, 'A')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _B:
                    pp = _ui.replace(_ui, 'B')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _C:
                    pp = _ui.replace(_ui, 'C')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _D:
                    pp = _ui.replace(_ui, 'D')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _E:
                    pp = _ui.replace(_ui, 'E')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _F:
                    pp = _ui.replace(_ui, 'F')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _G:
                    pp = _ui.replace(_ui, 'G')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _H:
                    pp = _ui.replace(_ui, 'H')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _I:
                    pp = _ui.replace(_ui, 'I')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _J:
                    pp = _ui.replace(_ui, 'J')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _K:
                    pp = _ui.replace(_ui, 'K')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _L:
                    pp = _ui.replace(_ui, 'L')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _M:
                    pp = _ui.replace(_ui, 'M')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _N:
                    pp = _ui.replace(_ui, 'N')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _O:
                    pp = _ui.replace(_ui, 'O')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _P:
                    pp = _ui.replace(_ui, 'P')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _Q:
                    pp = _ui.replace(_ui, 'Q')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _R:
                    pp = _ui.replace(_ui, 'R')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _S:
                    pp = _ui.replace(_ui, 'S')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _T:
                    pp = _ui.replace(_ui, 'T')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _U:
                    pp = _ui.replace(_ui, 'U')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _V:
                    pp = _ui.replace(_ui, 'V')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _W:
                    pp = _ui.replace(_ui, 'W')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _X:
                    pp = _ui.replace(_ui, 'X')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _Y:
                    pp = _ui.replace(_ui, 'Y')
                    _yu.append(pp)
                    _ui = ''
                elif _ui == _Z:
                    pp = _ui.replace(_ui, 'Z')
                    _yu.append(pp)
                    _ui = ''
                else:
                    print(f'Unknown Character found \'{_ui}\' !')
                    _ui = ''

    return ''.join(_yu)


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
