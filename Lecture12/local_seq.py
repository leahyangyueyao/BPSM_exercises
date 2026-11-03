renew_seq = open("/localdisk/data/BPSM/Lecture12/plain_genomic_seq.txt").read().upper()
renewline_seq = renew_seq.replace("\n","")
renewno_seq = (
    renewline_seq
    .replace("A","")
    .replace("T","")
    .replace("G","")
    .replace("C","")
)
print(renewno_seq)
#XSKLXXXXX
final_seq = (
    renewline_seq
    .replace("X","")
    .replace("S","")
    .replace("K","")
    .replace("L","")
)
print(final_seq)
#ATCGATCGATCGATCTGAGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT
exon1 = final_seq[0:63]
exon2 = final_seq[90:]
intron = final_seq[63:90]
len(final_seq)
#126
print(exon1)
#ATCGATCGATCGATCTGAGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGAT
print(exon2)
#GCTATCATCGATCGATATCGATGCATCGACTACTAT
print(intron)
#CGATCGATCGATCGATCGATCGATCAT

exon1_out = open("exon1.fasta", "w")
exon1_out.write(
    ">exon1_length"
    + str(len(exon1)) + "\n"
)
#16
exon1_out.write(exon1)
#63
exon1_out.close()

exon2_out = open("exon2.fasta", "w")
exon2_out.write(
    ">exon2_length"
    + str(len(exon2)) + "\n"
)
#16
exon2_out.write(exon2)
#36
exon2_out.close()

intron_out = open("intron.fasta", "w")
intron_out.write(
    ">intron_length"
    + str(len(intron)) + "\n"
)
#17
intron_out.write(intron)
#27
intron_out.close()
