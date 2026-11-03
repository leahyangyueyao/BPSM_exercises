import subprocess
import os
db = os.path.expanduser(“~/Exercises/Lecture06/nem")
queryseqs = “All_exons.fasta"
cmd = "blastx -db " + db + " -query " + queryseqs + " -outfmt 7"
subprocess.call(cmd, shell=True)
cmd = (
    "blastx -db " + db
    + " -query " + queryseqs
    + " -outfmt 6 -num_alignments 1"
)
result = subprocess.run(
    cmd,
    shell=True,
    capture_output=True,
    text=True,
    check=True
)
with open("blast_exons.out", "w") as output_file:
    output_file.write(result.stdout)
