#!/bin/env python
from string import maketrans


def rot(ch, off):
    return chr(((ord(ch) - 65 + off) % 26) + 65)


def brute_force2(data):
    for off in xrange(1, 26):
        print ' '.join([''.join([rot(e, off) for e in s]) for s in data.split(' ')])


def brute_force(raw_str):
    for i in range(1, 25):
        decryption_str = ''
        for s in raw_str:
            if s is not ' ':
                decryption_str += chr(((ord(s) - 65 + i) % 26 + 26) % 26 + 65)
            else:
                decryption_str += ' '
        # most_com_word = ['the', 'is', 'to', 'not', 'have', 'than', 'for', 'ok', 'and']
        # captial_most_com_word = [i.upper() for i in most_com_word]
        # for word in captial_most_com_word:
        #    if word in decryption_str:
        print decryption_str


def brute_force3(raw_str):
    inttable = "ABCDEFG"
    outtable = "BCDEFGH"
    trastable = maketrans(inttable, outtable)
    raw_str.traslate(trastable)


def brute_force4(input):
    input = 'KYV HLZTB SIFNE WFO ALDGJ FMVI KYV CRQP UFX FW TRVJRI REU PFLI LEZHLV JFCLKZFE ZJ UUUWSGGVFESC'
    shift = range(26)
    charlist = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for i in shift:
        def trans(x):
            if x not in charlist:
                return x
            else:
                if ord(x) + i > ord('Z'):
                    return chr(ord(x) + i - 26)
                else:
                    return chr(ord(x) + i)

        output = ''.join(map(trans, input)) #单个字符包括空格当做单个字符拆成字符数组 对每个字符进行trans 最后重新拼接。
        print output


data = 'UIF RVJDL CSPXO GPY KVNQT PWFS UIF MBAZ EPH EJ DFTBSF FE FDDP MB UVB TPMVAJPOF QFSTPOBMJAABUB TIQSNTSDHONO'

if __name__ == "__main__":
    raw_str = "MAX JNBVD UKHPG YHQ CNFIL HOXK MAX ETSR WHZ HY VTXLTK TGW RHNK NGBJNX LHENMBHG BL LEKWGXZFLFAE"
    # brute_force(raw_str)
    # brute_force2(raw_str)
    brute_force4(raw_str)
