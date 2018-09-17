###############################################################################
##
## File:        AlphaSig
## Author:      cwfietz
##
## Description: 
##
###############################################################################

from time import time
from datetime import timedelta

class AlphaSig:
    """
    Holds the signature of letters for a string.

    Takes a string and creates an array of counts of each letter.
    """
    def __init__(self, stringToSignature):
        """
        Takes in a string. Counts the letters.

        """
        # self.size = 0
        # self.empty = True
        self.signature = [0] * 26
        for eachLetter in stringToSignature:
            if eachLetter.isalpha():
                self.signature[ ord(eachLetter.upper()) - 65 ] += 1
        self.count_size()
    def count_size(self):
        """
        Sums the counts of all the letters together to one number and
        set the internal size attribute. Sets the internal empty attribute
        to True or False.
        """
        self.size = 0
        for eachCount in self.signature:
            self.size += eachCount
        if self.size == 0:
            self.empty = True
        else:
            self.empty = False
    def get_size(self):
        """
        Returns the size of the signature.
        """
        return self.size
    def is_empty(self):
        """
        Returns True if the signature is empty. False otherwise.
        """
        return self.empty
    def get_sig(self):
        """
        Returns a tuple of the 26 counts of letters of the signature.
        """
        return tuple(self.signature)
if __name__ == "__main__":
    """
    Code to test the methods of the AlphaSig class.
    """
    startTime = time()

    inputString = ['ghostlier','', 'Officially cancelled; Season 6 to air on another network.','The quick brown fox jumps over the lazy dog.']
    for eachString in inputString:
        x = AlphaSig(eachString)
        print(eachString, '=', x.signature)
        print('size =', x.get_size())
        print('length =', len(eachString))
        print('Signature:', x.get_sig())
        if x.is_empty():
            print(x, "is empty")
        else:
            print(x, 'is not empty.')

    endTime = time()
    d = timedelta( seconds = endTime-startTime )
    print( d )