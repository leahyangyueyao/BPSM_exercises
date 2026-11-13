def counts(dna, kmersize, minfrequency):
    dna = dna.upper()
    kmer_counts = {}
    for i in range(len(dna) - kmersize + 1):
        kmer = dna[i:i + kmersize]
        if kmer in kmer_counts:
            kmer_counts[kmer] += 1
        else:
            kmer_counts[kmer] = 1
    for kmer in kmer_counts:
        if kmer_counts[kmer] > minfrequency:
            print(kmer)

# Ask the user for input
dna = input("Enter DNA sequence: ")
kmersize = int(input("Enter k-mer length: "))
minfrequency = int(input("Enter minimum frequency: "))

count_kmers(dna, kmersize, minfrequency)
