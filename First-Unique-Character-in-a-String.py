#Given a string, find the first non-repeating character in it and return it's index.
# If it doesn't exist, return -1.

import collections


class solutionsFirtChar(object):

    def firstChar(self,s):
        count = collections.Counter(s)

        index = 0

        for ch in s:
            if count[ch] == 1:
                return index
            else:
                index = index + 1
        return -1



check = solutionsFirtChar()

verifycheck = check.firstChar("aaamttyy")

print(verifycheck)

