###############################################################################
##
## File:        find_word_signatures.py
## Author:      cwfietz
##
## Description: 
##
###############################################################################

from time import time, clock
from datetime import timedelta

def buildList():
    wordsList = []
    fin = open('dict1.txt')
    for line in fin:
        word = line.strip()
        wordsList.append( word ) # takes seconds
    return wordsList

def getSignature( w ):
    sig = [0] * 26
    for eachLetter in w:
        sig[ ord(eachLetter.upper()) - 65 ] += 1
    signature = tuple(sig)
    return signature

def main():
    wl = buildList()
    output = ''
    count = 0
    for eachWord in wl:
        count += 1
        s = getSignature( eachWord )
        output += '{:6} {:20} {}\n'.format(count, eachWord, s)
    print(output)

if __name__ == "__main__":
    startTime = time()
    main()
    endTime = time()
    # print( "startTime:", startTime )
    # print( "endtime:", endTime)
    # print( "endTime-startTime:", endTime-startTime )
    d = timedelta( seconds = endTime-startTime )
    print( d )

## dict1.txt
##  55 wore                 (0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0)
##  56 worse                (0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0)
##
##0:00:00.085655

## dict2.txt
##3926 yourself             (0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0)
##3927 zero                 (0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1)
##
##0:00:02.840328

## dict3.txt
##19910 zucchini             (0, 0, 2, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1)
##19911 zygote               (0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1)
##
##0:00:14.639180

## dict4.txt
##19910 quasicontinuous      (1, 0, 1, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 2, 0, 1, 0, 2, 1, 3, 0, 0, 0, 0, 0)
##19911 quasistationary      (3, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 1, 1, 0, 1, 1, 2, 2, 1, 0, 0, 0, 1, 0)
##
##0:00:14.572105

## words.txt
##113808 zymurgies            (0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1)
##113809 zymurgy              (0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 2, 1)
##
##0:01:38.812625
