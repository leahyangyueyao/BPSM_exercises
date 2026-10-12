#6. how many HSPs are shorter than 100 amino acids?
grep -v "#" blastoutput2.out | while IFS=$'\t' read -r qseqid sseqid pident length mismatches gapopen qstart qend sstart send evalue bitscore do
if [ "$length" -lt 100 ]; then
echo -e "$length"
fi
done | wc -l

#7. list the top ten highest (best) HSPs.
grep -v "#" blastoutput2.out | sort -t$'\t' -k12,12nr | head -n 10

#8. list the start positions of all matches where the HSP Subject accession includes the letters string "AEI"
grep -v "#" blastoutput2.out | cut -f2,7,9 | grep "AEI"

#9. how many subject sequences have more than one HSP?
grep -v "#" blastoutput2.out | cut -f2 | sort -d | uniq -c |
{
total=0
while read -r count sseqid;
do
if [ "$count" -gt 1 ]; then
((total++))
fi
done
echo -e "$total"
}

#10. what percentage of each HSP is made up of mismatches?
grep -v "#" blastoutput2.out | while IFS=$'\t' read -r qseqid sseqid pident length mismatches gapopen qstart qend sstart send evalue bitscore
do
pct=$(( mismatches * 100 / length ))
echo -e "${qseqid}\t${sseqid}\t${pct}%"
done

#11. allocate HSPs into a small number of different groups based on their scores (you choose which scores)
grep -v "#" blastoutput2.out | while IFS=$'\t' read -r qseqid sseqid pident length mismatches gapopen qstart qend sstart send evalue bitscore
do
score_int=$(echo "$bitscore" | cut -d'.' -f1)
if [ "$score_int" -ge 300 ]; then
echo -e "${qseqid}\t${sseqid}\t${pident}\t${length}\t${mismatches}\t${gapopen}\t${qstart}\t${qend}\t${sstart}\t${send}\t${evalue}\t${bitscore}" >> "${HOME}/BPSM_exercise/Lecture06/score300.txt"
fi
if [ "$score_int" -ge 200 ] && [ "$score_int" -lt 300 ]; then
echo -e "${qseqid}\t${sseqid}\t${pident}\t${length}\t${mismatches}\t${gapopen}\t${qstart}\t${qend}\t${sstart}\t${send}\t${evalue}\t${bitscore}" >> "${HOME}/BPSM_exercise/Lecture06/score200_300.txt"
fi
if [ "$score_int" -ge 100 ] && [ "$score_int" -lt 200 ]; then
echo -e "${qseqid}\t${sseqid}\t${pident}\t${length}\t${mismatches}\t${gapopen}\t${qstart}\t${qend}\t${sstart}\t${send}\t${evalue}\t${bitscore}" >> "${HOME}/BPSM_exercise/Lecture06/score100_200.txt"
fi
if [ "$score_int" -lt 100 ]; then
echo -e "${qseqid}\t${sseqid}\t${pident}\t${length}\t${mismatches}\t${gapopen}\t${qstart}\t${qend}\t${sstart}\t${send}\t${evalue}\t${bitscore}" >> "${HOME}/BPSM_exercise/Lecture06/score100.txt"
fi
done
