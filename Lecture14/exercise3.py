sequences = ["ATTGTACGG", "AATGAACCG", "AATGAACCC", "AATGGGAAT"]
for i in range(len(sequences)):
   for j in range(i+1,len(sequences)):
       seq1 = sequences[i]
       seq2 = sequences[j]
       sim = 0
       for position in range(len(seq1)):
           if seq1[position] == seq2[position]:
              sim += 1
              percentage = sim / len(seq1) *100
              print("Sequence",i+1,"and Sequence",j+1,":",percentage,"%")
