import string
import sys

def parsePolymer(polymer):
	i = 0
        while i < len(polymer) - 1:
            if (polymer[i].swapcase() == polymer[i+1]):
                polymer = polymer.replace(polymer[i:i+2], '')
                if i > 0:
                    i -= 1
            else:
                i += 1
	return polymer

def findBadUnit(polymer):
    lowest = sys.maxsize
    problemType = ''
    for letter in string.ascii_lowercase:
        testPolymer = polymer.replace(letter, '') # Strip lowercase occurrences
        testPolymer = testPolymer.replace(letter.upper(), '') # Strip uppercase occurences
        testPolymer = parsePolymer(testPolymer) 
        if len(testPolymer) < lowest:
            lowest = len(testPolymer)
            problemType = letter
    return problemType, lowest

assert parsePolymer("dabAcCaCBAcCcaDA") == 'dabCBAcaDA'
assert parsePolymer("dabAcCaCBAcCcaDAa") == 'dabCBAcaD'
input = open('input.txt', 'r').read().strip()
print 'Part 1: the number of units remaining in the parsed polymer is: %i.' % (len(parsePolymer(input)))
assert findBadUnit("dabAcCaCBAcCcaDA") == ('c', 4)
output = findBadUnit(input)
print 'Part 2: %s is the problem type, removing it results in a polymer of length %i.' % (output[0], output[1])
