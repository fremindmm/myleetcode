#!/bin/env python
import os
from itertools import izip
def mergeTowFile(f1,f2,filelist):
    if not f2:
        return 0
    with open(f2, 'rb') as f2obj:
        with open(f1,'ab') as f1obj:
            f1obj.write(f2obj.read())
    os.remove(f2)
    filelist.pop(filelist.index(f2))


def pairwise(iterable):
    "s -> (s0, s1), (s2, s3), (s4, s5), ..."
    a = iter(iterable)
    return izip(a, a)



if __name__=='__main__':
    tmpfile=os.getcwd()+'/tmp/'
    os.chdir(tmpfile)
    pwdc=os.getcwd()
    while True:
        filelist=os.listdir(pwdc)
        if len(filelist) < 2:
            break
        if len(filelist)/2 !=0:
            filelist.append('')
            newfilelist=filelist[:]
        for x, y in pairwise(newfilelist):
            mergeTowFile(x,y,filelist) 
    
