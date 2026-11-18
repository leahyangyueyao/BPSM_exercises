def run_query(sql):
    result = pd.read_sql_query(sql, db_engine)
    print(result.to_string(index=False))
    return result
#how many fungal species have genomes bigger than 100Mb? What are their names?
sql = """
SELECT COUNT(DISTINCT `#Organism/Name`) AS species_count
FROM eukaryotes
WHERE `Group` = 'Fungi'
  AND `Size (Mb)` > 100;
"""

run_query(sql)
#how many of each Kingdom/group (plants, animals, fungi and protists) have been sequenced?
sql = """
SELECT `Group`, COUNT(*) AS genome_count
FROM eukaryotes
WHERE `Group` IN ('Plants', 'Animals', 'Fungi', 'Protists')
GROUP BY `Group`
ORDER BY genome_count DESC;
"""

run_query(sql)
#which Heliconius species genomes have been sequenced?
sql = """
SELECT DISTINCT `#Organism/Name`
FROM eukaryotes
WHERE `#Organism/Name` LIKE 'Heliconius%'
ORDER BY `#Organism/Name`;
"""

run_query(sql)
#which sequencing centre has sequenced the most plant genomes? the most insect genomes?
sql = """
SELECT `Center`,COUNT(*) AS genome_count
FROM eukaryotes
WHERE `Group` = 'Plants'
GROUP BY `Center`
ORDER BY genome_count DESC
LIMIT 1;
"""

run_query(sql)

sql = """
SELECT `Center`,COUNT(*) AS genome_count
FROM eukaryotes
WHERE `SubGroup` = 'Insects'
GROUP BY `Center`
ORDER BY genome_count DESC
LIMIT 1;
"""

run_query(sql)
#add a column giving the number of proteins per gene. Which genomes have at least 10% more proteins than genes?
sql = """
SELECT `#Organism/Name`, `Genes`, `Proteins`, `Proteins` / `Genes` AS Proteins_per_gene
FROM eukaryotes
WHERE `Proteins` >= 1.1 * `Genes`
  AND `Genes` > 0
ORDER BY Proteins_per_gene DESC;
"""

run_query(sql)
