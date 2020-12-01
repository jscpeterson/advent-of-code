import re

class Claim:
    """A single elf claim"""
    
    claimId = 0
    claimLeft = 0
    claimTop = 0
    claimWidth = 0
    claimHeight = 0
    adjustedWidth = 0
    adjustedHeight = 0

    def __init__(self, claim):
        self.claimId = int(re.findall(r'(?<=#)\d+', claim)[0])
        self.claimLeft = int(re.findall(r'(?<=@ )\d+', claim)[0]) 
        self.claimTop = int(re.findall(r'(?<=,)\d+', claim)[0])
        self.claimWidth = int(re.findall(r'(?<=: )\d+', claim)[0])
        self.claimHeight = int(re.findall(r'(?<=x)\d+', claim)[0])
        
    def __str__(self):
        return "#%i @ %i,%i: %ix%i" % (self.claimId, self.claimLeft, self.claimTop, self.claimWidth, self.claimHeight)

  
def populate(filename):
    outputs = []
    with open(filename) as f:
       for line in f:
           line = line.strip('\n')
           outputs.append(line)
       else:
        # No more lines to be read from file
           return outputs
           

rawClaims = populate("input.txt")
claims = []
for s in rawClaims:
    claims.append(Claim(s))
for claim in claims:
    print claim
