for start in range(100, 1000, 100):
    end = start + 99
    folder = str(start) + "-" + str(end)
    os.makedirs(folder, exist_ok=True)

with open("xaa.dna", "r") as infile:
    for line in infile:
        dna = line.strip()
        print(len(dna))

lengths = [333, 283, 380, 115, 753, 764, 234, 117, 906, 160]

for length in lengths:
    lower = (length // 100) * 100
    upper = lower + 99
    folder = str(lower) + "-" + str(upper)
