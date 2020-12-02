import string;

#Part 1
def checksumStrings(stringArray):
    checksum1 = 0 # 2 sums
    checksum2 = 0 # 3 sums
    charDict = {}
    for s in stringArray:
        for char in string.ascii_lowercase:
            charDict[char] = 0
        for char in s:
            charDict[char] = charDict[char] + 1
        if 2 in charDict.values():
            checksum1 += 1
        if 3 in charDict.values():
            checksum2 += 1
    return checksum1 * checksum2

#Part 2
def findString(stringArray):
    pastStrings = set();
    for s in stringArray:
        for pastString in pastStrings:
            mismatches = 0
            mismatchIndex = 0
            for i in range(0, len(pastString)):
                if s[i] != pastString[i]:
                    mismatchIndex = i
                    mismatches += 1
            if mismatches == 1:
                return s[:mismatchIndex] + s[mismatchIndex+1:] #strips char from a specific index
        pastStrings.add(s)
    
def populateFile(filename):
    outputs = []
    with open(filename) as f:
       for line in f:
           line = line.strip('\n')
           outputs.append(line)
       else:
        # No more lines to be read from file
           return outputs

values = populateFile("input.txt")
print "Checksum: %i" % (checksumStrings(values))
print "ID: %s" % (findString(values))

