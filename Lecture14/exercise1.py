with open("data.csv","r") as infile:
    for line in infile:
       #remove newline and split columns
       data = line.strip().split(",")
       species = data[0].strip()
       sequences = data[1].strip().upper()
       gene = data[2].strip()
       expression = float(data[3])
       #Print out the gene names for all genes from the species Drosophila melanogaster or Drosophila simulans.
       if species == "Drosophila melanogaster" or species == "Drosophila simulans":
          print("Q1:",gene)
       #Print out the gene names for all genes that are between 90 and 110 bases long.
       length = len(sequences)
       if 90 <= length <= 110:
          print("Q2:",gene)
       #Print out the gene names for all genes whose AT content is less than 0.5 and whose expression level is greater than 200.
       AT_content = (sequences.count("A") + sequences.count("T"))/length
       if AT_content < 0.5 and expression > 200:
          print("Q3:",gene)
       #Print out the gene names for all genes whose name begins with "k" or "h" except those belonging to Drosophila melanogaster.
       if (gene.lower().startswith("k") or gene.lower().startswith("h") and species != "Drosophila melanogaster":
          print("Q4:",gene)
       #For each gene, print out a message giving the gene name and saying whether its AT content is high (greater than 0.65), low (less than 0.45) or medium (between 0.45 and 0.65).
       if AT_content > 0.65:
          print("high AT content:",gene)
       elif AT_content < 0.45:
            print("Low AT content:",gene)
       else:
            print("Medium AT content:",gene)
