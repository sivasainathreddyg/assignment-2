i=int(input('enter the total number of alphabet'))
asciidict=dict()
alfha=range(97,97+i)
for i in alfha:
        asciidict[chr(i)]=i
print(asciidict)