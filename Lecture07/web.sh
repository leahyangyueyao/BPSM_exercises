esearch -db nucleotide -query "Cosmoscarta[organism]"
esearch -db nucleotide -query "Cosmoscarta[organism]" | efetch -format fasta > Cosmoscarta.nuc.fa
grep -c ">" Cosmoscarta.nuc.fa

esearch -db protein \
  -query 'HOXA7[Gene Name] AND Primates[Organism]' \
  | efetch -format fasta \
  > hoxa7_primates.fasta
grep -c ">" hoxa7_primates.fasta
head -n 20 hoxa7_primates.fasta

# 窗口大小为 4
plotcon \
  -sequence hoxa7_primates.fasta \
  -winsize 4 \
  -graph png \
  -goutfile hoxa7_plot_w4.png
# 窗口大小为 10
plotcon \
  -sequence hoxa7_primates.fasta \
  -winsize 10 \
  -graph png \
  -goutfile hoxa7_plot_w10.png
# 窗口大小为 20
plotcon \
  -sequence hoxa7_primates.fasta \
  -winsize 20 \
  -graph png \
  -goutfile hoxa7_plot_w20.png
