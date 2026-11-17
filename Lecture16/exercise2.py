gencode = {
'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}
def translate(dna):
   protein = ""
   dna = dna.upper()
   for i in range(0,len(dna),3):
      codon = dna[i:i+3]
      amino_acid = gencode.get(codon,"X")
      protein = protein + amino_acid
   return protein

def reverse_complement(dna):
   complement = {"A":"T","T":"A","C":"G","G":"C","N":"N"}
   reverse_dna = dna.upper()[::-1]
   result = ""
   for base in reverse_dna:
       result = result + complement[base]
   return result

dna = input("Enter a DNA sequence:").upper

for frame in range(3):
   sequence = dna[frame:]
   protein = translate(sequence)
   print("Forward frames",frame+1,":",protein)

reverse_dna = reverse_complement(dna)

for frame in range(3):
   sequence = reverse_dna[frames:]
   protein = translate(sequence)
   print("Reverse frames",frame+1,":",protein)
