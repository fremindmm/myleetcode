
# follow.py
#
# Follow a file like tail -f.

import time
def follow(thefile):
    thefile.seek(0,2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

def read_revese(filename,t):
    filename.seek(0, 2)
    count = 0
    while True:
        line = filename.readline()
        if not line:
            time.sleep(0.1)
            count += 1
            if count*0.1 == t:
                print "timeout"
                break
            continue
        yield line


if __name__ == '__main__':
#    logfile = open("run/foo/access-log","r")
#    loglines = follow(logfile)
    lf = open('/Users/benben/Documents/myleetcode/file/log.txt','r')
    lfs = read_revese(lf, 10)
    for line in lfs:
        print line,
