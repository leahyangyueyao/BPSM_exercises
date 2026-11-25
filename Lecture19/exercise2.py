import matplotlib.pyplot as plt
def plot_content(window=1000, content="AT", start=0, end=None, filename="ecoli.txt"):

    with open(ecoli.txt) as infile:
         genome = infile.read()

    genome = genome.replace("\n", "").upper()
    sequence = genome[start:end]
    values = []
    positions = []
    for i in range(len(sequence) - window + 1):
        win = sequence[i:i + window]
        if content == "AT":
            fraction = (win.count("A") + win.count("T")) / window
        else:
            fraction = (win.count("G") + win.count("C")) / window
        values.append(fraction)
        positions.append(start + i)

    plt.figure(figsize=(20, 10))
    plt.plot(positions, values, label=content + " content")
    plt.xlabel("Position on genome")
    plt.ylabel(content + " fraction")
    plt.title(content + " content in the E. coli genome")
    plt.legend
    plt.savefig(content + "_content.png", transparent=True)
    plt.show()


window = int(input("Enter window size: "))
content = input("Enter AT or GC: ").upper()
start = int(input("Enter genome start: "))
end = int(input("Enter genome end: "))
plot_content(window, content, start, end)
