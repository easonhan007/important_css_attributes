# USAGE: ./attr.sh *.css
echo $1
cat $1 | grep  ';' | tr -d ' ' | cut -d ':' -f 1 | sort | grep -v "^-" | grep -v "^/"| grep -v "^\."| grep -v "^\*"|grep -v "^@"| grep -v "^\s"|uniq -c | sort -r
