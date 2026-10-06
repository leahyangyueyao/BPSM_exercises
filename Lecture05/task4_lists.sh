index=0
count=0
while IFS=$'\t' read -r name    email   city    birthday_day    birthday_month  birthday_year   country;
> do
> ((index++))
> if ((index == 1));then
> continue
> fi
> if [[ -z "${name}" ]];then
> continue
> fi
> if [[ "$birthday_month" == "10" ]];then
> ((count++))
> echo -e “${count}\t${name}\t${city}\t${country}"
> fi
> done < example_people_data.tsv
#结果
1	Celeste	Stirling	Grenada
2	Vivien	Kenosha	Sao Tome and Principe
3	Bruce	Somma Lombardo	Afghanistan
4	Berk	Otricoli	Congo (Brazzaville)
5	Leilani	Rosarno	Japan
6	Isadora	Strausberg	Trinidad and Tobago
7	Veronica	St. Thomas	Western Sahara
8	Fulton	Juazeiro do Norte	Brunei
9	Cally	Rocky View	Mozambique
10	Dominique	Castel Baronia	Guinea
11	Grace	Cisterna di Latina	Antigua and Barbuda
