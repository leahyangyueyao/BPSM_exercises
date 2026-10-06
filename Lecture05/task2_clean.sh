index=0
count=0
while IFS=$'\t' read -r name    email   city    birthday_day    birthday_month  birthday_year   country;
> do
> ((index++))
> if ((index == 1));then
> continue
> fi
> if ((index == 102 ));then
> break
> fi
> count=$((count+1))
> echo -e "${count}\t${name}\t${city}\t${country}"
> done < example_people_data.tsv
