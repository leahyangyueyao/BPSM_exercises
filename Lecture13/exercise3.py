import os
#read the sequence
with open("remote_cds.fasta","r") as infile:
    dna = ""
    for line in infile:
       if not line.startswith(">"):
         dna += line.strip().upper()

window_size = 30
offset = 3

os.mkdir("individual_windows",exist_ok=TRUE)

with open("all_windows.fasta","w") as combfile:
    for start in range(0,len(dna),offset):
       stop = start + window_size
       segment = dna[start:stop]
       print("Start:",start)
       print("Sequence:",segment)
#gc count
       gc_count = segment.count("G") + segment.count("C")
       gc_percentage = gc_count/len(segment) * 100
       print("GC percentage:",gc_percentage)
#individual fasta file
       header = ">AJ223353_window_{start+1}_{start+len(segment)}"
       filename = "individual_windows_{start+1}.fasta"
       with open(filename,"w") as outfile:
           outfile.write(header + "\n")
           outfile.write(segment + "\n")
#single fasta file
           combfile.write(header + "\n")
           combfile.write(segment + "\n")
