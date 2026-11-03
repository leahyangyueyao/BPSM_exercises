wget -qO AJ223353.fasta "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=AJ223353&rettype=fasta&retmode=text"
cat AJ223353.fasta
grep -v ">" AJ223353.fasta > AJ223353_noheader.fasta
p3
remotefile = open("AJ223353_noheader.fasta").read().upper()
renewremotefile = remotefile.replace(“\n","")
remote_noncoding1 = renewremotefile[0:28]
remote_cds = renewremotefile[28:409]
remote_noncoding2 = renewremotefile[409:]

remote_noncoding1_out = open("remote_noncoding1.fasta","w")
remote_noncoding1_out.write(
    ">AJ223353_noncoding1_length"
    +str(len(remote_noncoding1)) + "\n"
)
#30
remote_noncoding1_out.write(remote_noncoding1)
#28
remote_noncoding1_out.close()

remote_cds_out = open("remote_cds.fasta", "w")
remote_cds_out.write(
    ">AJ223353_cds_length"
    + str(len(remote_cds)) + "\n"
)
#24
remote_cds_out.write(remote_cds)
#381
remote_cds_out.close()

remote_noncoding2_out = open("remote_noncoding2.fasta", "w")
remote_noncoding2_out.write(
    ">AJ223353_noncoding2_length"
    + str(len(remote_noncoding2)) + "\n"
)
#31
remote_noncoding2_out.write(remote_noncoding2)
#399
remote_noncoding2_out.close()
