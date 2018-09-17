###############################################################################
##
## File:        saveDictOfSignatures.py
## Author:      cwfietz
##
## Description: 
##
###############################################################################

from time import time, clock
from datetime import timedelta
from pickle import dump

def buildList():
    wordsList = []
    fin = open('words.txt')
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
    
##    # Write results to file
##    with open('output.txt', 'w') as f:
##        f.write(output)
##        f.write('\n')
##        for eachItem in sigDict.items():
##            f.write( str( eachItem) + '\n')
##    f.closed
##
##    with open('anagram.txt', 'w') as f:
##        for eachKey in iter(sigDict):
##            if len( sigDict[eachKey] ) >= 2:
##                f.write( str( eachKey ) + ' ' + str( sigDict[eachKey] ) + '\n')
##    f.closed

    dump( sigDict , open( "sigDict_words.p", "wb" ) )    

if __name__ == "__main__":
    startTime = time()
    main()
    endTime = time()
    # print( "startTime:", startTime )
    # print( "endtime:", endTime)
    # print( "endTime-startTime:", endTime-startTime )
    d = timedelta( seconds = endTime-startTime )
    print( d )
