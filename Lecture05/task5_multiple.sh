index=0
count=0
mkdir -p birthday_output
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
> echo -e “${count}\t${name}\t${city}\t${country}” >> ${HOME}/BPSM_exercise/Lecture05/birthday_output/October_${country}.txt
> fi
> done < example_people_data.tsv
