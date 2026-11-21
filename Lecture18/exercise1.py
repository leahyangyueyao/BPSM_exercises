import re
accession = ['xkn59438', 'yhdck2', 'eihd39d9', 'chdsye847', 'hedle3455', 'xjhd53e', '45da', 'de37dp']
#contain the number 5
for target in accession:
    if re.search(r'5',target):
        print(target)
#xkn59438、hedle3455、xjhd53e、45da

#contain the letter d or e
for target in accession:
    if re.search(r'[de]',target):
        print(target)
#yhdck2, eihd39d9, chdsye847, hedle3455, xjhd53e, 45da, de37dp

#contain the letters d and e in that order
for target in accession:
    if re.search(r'd.*e',target):
        print(target)
#chdsye847,hedle3455,xjhd53e,de37dp

#contain the letters d and e in that order with a single letter between them
for target in accession:
    if re.search(r'd[a-z]e',target):
       print(target)
#hedle3455

#contain both the letters d and e in any order
for target in accession:
    if re.search(r'd.*e|e.*d',target):
       print(target)
#eihd39d9,chdsye847,hedle3455,xjhd53e,de37dp

#start with x or y
for target in accession:
    if re.search(r'^[xy]',target):
       print(target)
#xkn59438,yhdck2,xjhd53e

#start with x or y and end with e
for target in accession:
    if re.search(r'^[xy].*e$',target):
       print(target)
#xjhd53e

#contains any 3 numbers in any order
for target in accession:
    if re.search(r'\d.*\d.*\d',target):
       print(target)
#xkn59438,eihd39d9,chdsye847,hedle3455

#contains 3 different numbers in the accession
for target in accession:
    prob = re.findall(r'd',target)
    if len(set(prob)) >= 3:
       print(target)
#xkn59438,chdsye847,hedle3455

#contain three or more numbers in a row
for target in accession:
    if re.search(r'\d{3,}',target):
       print(target)
#xkn59438,chdsye847,hedle3455

#end with d followed by either a, r or p
for target in accession:
    if re.search(r'd[arp]$',target):
       print(target)
#45da,de37dp
