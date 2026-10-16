cat mock_NCBI.fasta | awk 'BEGIN{count=0;}{
if(substr($1,1,1)==">")
{
count++;
# Is this the first sequence?
if(count==1)
{
# No new line needed
printf $1"\n";
}
else{
# Line needed as not the first sequence
printf "\n"$1"\n";
}
}
# That wasn't the fasta header line
else {
printf $1;
}  # else loop
}  # action loop
# All done, so do the last line
END{
printf "\n";
}'              > singleline_NCBIseqs.fasta
