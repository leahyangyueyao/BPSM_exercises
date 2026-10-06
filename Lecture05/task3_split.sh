index=0
mkdir -p output
while IFS=$'\t' read -r name    email   city    birthday_day    birthday_month  birthday_year   country;
> do
> ((index++))
> if ((index == 1));then
> continue
> fi
#-z检查一个字符串是否为空（zero)
> if [[ -z "${name}" ]];then
> continue
> fi
> echo -e "${name}\t${email}\t${city}\t${birthday_day}\t${birthday_month}\t${birthday_year}\t${country}" >> ${HOME}/BPSM_exercise/Lecture05/output/${country}.txt
> done < example_people_data.tsv
