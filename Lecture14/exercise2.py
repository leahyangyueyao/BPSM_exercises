#k-mer counting
dna="ATGCATCATG"
k=2 # kmer size
n=2 # more than this number found
kmer_counts = {}
#sliding window
for i in range(len(dna) -k +1):
   kmer = dna[i:i+k]
   if kmer in kmer_counts:
      kmer_counts[kmer] += 1
   else:
      kmer_counts[kmer] = 1
#print more than n
for kmer in kmer_counts:
   if kmer_counts[kmer] > n:
      print(kmer,kmer_counts[kmer])
