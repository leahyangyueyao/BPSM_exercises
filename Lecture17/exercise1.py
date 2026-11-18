#how many fungal species have genomes bigger than 100Mb? What are their names?
df = pd.read_csv('eukaryotes.txt', sep="\t", na_values=['-'])
fungal = df[(df['Group'] == 'Fungi') & (df['Size (Mb)'] > 100)]
unique_fungi = fungal['#Organism/Name'].unique()
pd.Series(unique_fungi, name='#Organism/Name')
len(unique_fungi)
#143

#how many of each Kingdom/group (plants, animals, fungi and protists) have been sequenced?
group_counts = df['Group'].value_counts()
print(group_counts)
#Fungi       16876
#Animals     14495
#Plants       4390
#Protists     1987
#Other         202

#which Heliconius species genomes have been sequenced?
heliconius = df[df['#Organism/Name'].str.startswith('Heliconius',na=False)]
print(heliconius['#Organism/Name'].unique())

#which sequencing centre has sequenced the most plant genomes? the most insect genomes?
plants = df[df['Group'] == 'Plants']
insects = df[df['SubGroup'] == 'Insects']
plant_center = plants['Center'].value_counts().sort_values(ascending=False).head(1)
insect_center = insects['Center'].value_counts().sort_values(ascending=False).head(1)
print("Plants:",plant_center)
#Plants: Center
#USDA-ARS    314
print("Insects:",insect_center)
#Insects: Center
#WELLCOME SANGER INSTITUTE    1637

#add a column giving the number of proteins per gene. Which genomes have at least 10% more proteins than genes?
df['Proteins_per_gene'] = df['Proteins'] / df['Genes']
target = df[df['Proteins_per_gene'] >= 1.1]
print(target[['#Organism/Name','Proteins_per_gene']])
