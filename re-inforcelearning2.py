import collections



class FirstUniqueChar(object):

    def solutionsfirstUniq(self, input):

        input = input.upper()

        count = collections.Counter(input)

        index = 0

        for ch in input:
            if count[ch] == 1:
                return index
            else:
                index += 1
        return -1


test = FirstUniqueChar()

test2 = test.solutionsfirstUniq("mmaartins")

print(test2)























