def findFrequency(values):
    i = 0
    count = 0
    frequency = 0
    freqs = set()
    while True:
        #print "%i: %i" % (count, frequency)
        if frequency in freqs:
            return frequency
        freqs.add(frequency)
        frequency += values[i]
        i += 1
        if i == len(values):
            i = 0
            count += 1
            print "Run %i: Reached end of dataset" % (count) 
        
def populateFile(filename):
    outputs = []
    with open(filename) as f:
       for line in f:
           outputs.append(int(line))
       else:
        # No more lines to be read from file
           return outputs

values = populateFile("input.txt")
finalFreq = findFrequency(values)
print "Found frequency: %i" % (finalFreq)
