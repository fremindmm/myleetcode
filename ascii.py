#!/bin/env python

str_list = [84, 104, 101, 32, 115, 111, 108, 117, 116, 105, 111, 110, 32, 105, 115, 58, 32, 108, 111, 115, 98, 115, 105, 104, 104, 114, 97, 109, 99]
ret= ''.join(map(chr, str_list))
print ret

python -c "print ''.join([chr(i) for i in [84, 104, 101, 32, 115, 111, 108, 117, 116, 105, 111, 110, 32, 105, 115, 58, 32, 111, 114, 110, 110, 108, 114, 99, 97, 100, 115, 101, 104]])"

import sys
#get the required numbers to convert from the input
line = sys.argv[1:]
finalString = "";
for ch in line:
        #remove the ','
        x = ch.replace(",", "")
        # convert the number(currently held as a string) to int and then get the ascii char corresponding to the int
        finalString+= chr(int(x))
print finalString
