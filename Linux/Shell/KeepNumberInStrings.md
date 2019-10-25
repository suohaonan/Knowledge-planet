#保留字符串中的数字，其它全去掉

把2007.10.30 16:00:00去掉"." ":" 和" "空格，生成20071030160000

1）echo "2007.10.30 16:00:00" |  awk -F'[.: ]'  '{for(i=1;i<=NF;i++)printf $i;}END {printf "\n"}'

2）sed 's/[^0-9]//g

3）tr -cd '[0-9]'

4）awk -F'[^0-9]' -vOFS= 'NF+=0' file

5）tr -d "[:punct:]|[:space:]"

转自：https://www.iteye.com/blog/fyan-1454067
