def amino_acid_percentages(protein,amino_acid):
    protein = protein.upper()
    amino_acid = amino_acid.upper()
    length = len(protein)
    count = protein.count(amino_acid)
    percentages = count/length *100
    return(percentages)

assert round(amino_acid_percentages("MSRSLLLRFLLFLLLLPPLP", "M")) == round(5)
assert round(amino_acid_percentages("MSRSLLLRFLLFLLLLPPLP", "r")) == round(10)
assert round(amino_acid_percentages("MSRSLLLRFLLFLLLLPPLP", "L")) == round(50)
assert round(amino_acid_percentages("MSRSLLLRFLLFLLLLPPLP", "Y")) == round(0)
