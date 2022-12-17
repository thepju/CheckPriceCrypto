s = "[1:one][2:two][3:three][4:four]"
d = input()
sidx = s.find(d) + 0 
eidx = s.find("]",sidx)
print(s[sidx: eidx+ 0 ])