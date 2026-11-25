import matplotlib.pyplot as plt

with open("ecoli.txt") as infile:
     ecoli = infile.read()

ecoli = ecoli.replace("\n","").upper()
window = 1000

#for the whole genome
at = []
for start in range(len(ecoli)-window+1):
    win = ecoli[start:start+window]
    at_content = (win.count("A") + win.count("T"))/window
    at.append(at_content)

plt.figure(figsize=(20,10))
plt.plot(at,color="green",label="AT content")
plt.xlabel("Position on genome")
plt.ylabel("AT fraction")
plt.title("AT content of the first whole genome")
plt.savefig("AT_whole.png",transparent=True)
plt.show

