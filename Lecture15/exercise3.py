def base_counter(dna,threshold=0.2):
   dna = dna.upper()
   count = 0
   for base in dna:
       if base not in "ATGC":
          count += 1
   percentage = count/len(dna)
   if percentage > threshold:
      return True
   else:
      return False

assert base_counter("ATGCATGC") == False
assert base_counter("ATGCATGCXXX") == True
