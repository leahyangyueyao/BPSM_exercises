exons_out = open("All_exons.fasta", "w")
exons_out.write(
    ">AJ223353_cds_length" + str(len(remote_cds))
    + "\n" + remote_cds + "\n"
)
#406
exons_out.write(
    ">exon1_length" + str(len(exon1))
    + "\n" + exon1 + "\n"
)
#80
exons_out.write(
    ">exon2_length" + str(len(exon2))
    + "\n" + exon2 + "\n"
)
#53
exons_out.close()

introns_out = open("All_noncodings.fasta", "w")
introns_out.write(
    ">AJ223353_noncoding1_length"
    + str(len(remote_noncoding1))
    + "\n" + remote_noncoding1 + "\n"
)
#59
introns_out.write(
    ">AJ223353_noncoding2_length"
    + str(len(remote_noncoding2))
    + "\n" + remote_noncoding2 + "\n"
)
#431
introns_out.write(
    ">intron_length"
    + str(len(intron))
    + "\n" + intron + "\n"
)
#45
introns_out.close()
