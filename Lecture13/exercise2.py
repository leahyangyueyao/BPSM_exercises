with open("genomic_dna2.txt","r") as infile:
    dna = infile.read().replace("\n","")
coding_sequence = []
with open("exons.txt","r") as infile:
    for line in infile:
        start, stop = line.strip().split(",")
        start = int(start)
        stop = int(stop)
        exon = dna[start:stop]
        coding_sequence.append(exon)
with open("coding_dna.txt","w") as outfile:
     outfile.write("".join(coding_sequence))
