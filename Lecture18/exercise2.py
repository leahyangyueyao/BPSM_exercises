import re

with open("long_dna.txt") as file:
     dna = file.read().replace("\n","").upper()

cuts = [0,len(dna)]

#What fragment lengths will we get if we digest the sequence with a novel restriction enzyme BpsmI, whose recognition site is ANT*AAT, where * indicates the position of the cut site.
for match in re.finditer(r'(?=A[ATGC]TAAT)',dna):
    cut_position = match.start() + 3
    cuts.append(cut_position)

cuts = sorted(set(cuts))

print(cuts)
#[0, 1143, 1628, 2012]

for i in range(len(cuts)-1):
    start = cuts[i]
    end = cuts[i+1]
    length = end - start
    print(length)
#1143,485,384

#What will the fragment lengths be if we do a double digest with both BpsmI and BpsmII (whose recognition site is GCRW*TG)?
for match in re.finditer(r'(?=A[ATGC]TAAT)',dna):
    cut_position = match.start() + 3
    cuts.append(cut_position)

for match in re.finditer(r'(?=GC[AG][AT]TG)', dna):
    cut_position = match.start() + 4
    cuts.append(cut_position)

cuts = sorted(set(cuts))

print(cuts)
#[0, 488, 1143, 1577, 1628, 2012]

for i in range(len(cuts)-1):
    start = cuts[i]
    end = cuts[i+1]
    length = end - start
    print(length)
#488,655,434,51,384

#What are the sequences of the fragments themselves?
for i in range(len(cuts)-1):
    start = cuts[i]
    end = cuts[i+1]
    fragment = dna[start:end]
    print(fragment)
