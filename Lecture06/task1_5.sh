#1. list the subject accession for all HSPs
grep -v "#" blastoutput2.out | cut -f2

#2. list the alignment length and percent ID for all HSPs
grep -v "#" blastoutput2.out | cut -f3,4

#3. show the HSPs with more than 20 mismatches
grep -v "#" blastoutput2.out | while IFS=$'\t' read -r qseqid sseqid pident length mismatches gapopen qstart qend sstart send evalue bitscore
do
if [ "$mismatches" -gt 20 ]; then
echo -e "${qseqid}\t${sseqid}\t${pident}\t${length}\t${mismatches}\t${gapopen}\t${qstart}\t${qend}\t${sstart}\t${send}\t${evalue}\t${bitscore}"
fi
done

#4. show the HSPs shorter than 100 amino acids and with more than 20 mismatches
grep -v "#" blastoutput2.out | while IFS=$'\t' read -r qseqid sseqid pident length mismatches gapopen qstart qend sstart send evalue bitscore
do
if [ "$length" -lt 100 ] && [ "$mismatches" -gt 20 ]; then
echo -e "${qseqid}\t${sseqid}\t${pident}\t${length}\t${mismatches}\t${gapopen}\t${qstart}\t${qend}\t${sstart}\t${send}\t${evalue}\t${bitscore}"
fi
done

#5. list the first 20 HSPs that have fewer than 20 mismatches
grep -v "#" blastoutput2.out | while IFS=$'\t' read -r qseqid sseqid pident length mismatches gapopen qstart qend sstart send evalue bitscore; 
do
if [ "$mismatches" -lt 20 ]; then
echo -e "${qseqid}\t${sseqid}\t${pident}\t${length}\t${mismatches}\t${gapopen}\t${qstart}\t${qend}\t${sstart}\t${send}\t${evalue}\t${bitscore}"; 
fi;
done | head -n 20
