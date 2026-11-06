with open("input.txt", "r") as infile, open("cleaned.txt", "w") as outfile:
        for line in infile:
            dna = line[14:].rstrip("\n")
            outfile.write(dna + "\n")
            print(len(dna))
#43 42 38 37 49 48 34 33 48 47
