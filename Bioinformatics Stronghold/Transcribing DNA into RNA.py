from string import maketrans   # Required to call maketrans function.

intab = "T"
outtab = "U"
trantab = maketrans(intab, outtab)

str = "GATGGAACTTGACTACGTAAATT";
print(str.translate(trantab))
