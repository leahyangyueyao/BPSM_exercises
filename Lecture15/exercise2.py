def amino_acid_percentages2(protein,amino_acids=["A","I","L","M","F","W","Y","V"]):
   protein = protein.upper()
   total_count = 0
   for amino_acid in amino_acids:
       count = protein.count(amino_acid.upper())
       total_count = total_count + count
   percentage = (total_count/len(protein)) * 100
   return percentage

assert round(amino_acid_percentages2("MSRSLLLRFLLFLLLLPPLP", ["M"])) == 5
assert round(amino_acid_percentages2("MSRSLLLRFLLFLLLLPPLP", ['F', 'S', 'L'])) == 70
assert round(amino_acid_percentages2("MSRSLLLRFLLFLLLLPPLP")) == 65
