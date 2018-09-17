###############################################################################
##
## File:        buildDictOfSignatures.py
## Author:      cwfietz
## Version:     
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
    sigDict = dict()
    for eachWord in wl:
        count += 1
        s = getSignature( eachWord )
        if s not in sigDict:
            sigDict[ s ] = [eachWord]
        else:
            sigDict[ s ] = sigDict[ s ] + [eachWord] ## yucky
            output += 'anagram?\n'
        output += '{:6} {:20} {}\n'.format(count, eachWord, s)        
    # print(output)
    # print()
    # print( sigDict )
    
    # Write results to file
    with open('output.txt', 'w') as f:
        f.write(output)
        f.write('\n')
        for eachItem in sigDict.items():
            f.write( str( eachItem) + '\n')
    f.closed

if __name__ == "__main__":
    startTime = time()
    main()
    endTime = time()
    # print( "startTime:", startTime )
    # print( "endtime:", endTime)
    # print( "endTime-startTime:", endTime-startTime )
    d = timedelta( seconds = endTime-startTime )
    print( d )

# Run times
# dict1.txt: 0:00:00.003114
# dict2.txt: 0:00:00.117880
# dict3.txt: 0:00:00.609891
# dict4.txt: 0:00:00.603560
# words.txt: 0:00:03.830042
