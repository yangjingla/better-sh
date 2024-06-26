
set -x


# == 
du -sh 1

# == 
tree -Lh 2


# ==
realpath filename 

# ==
time_stamp=$(date +'%Y%m%d_%H:%M:%S')


# ==

ls -d "output_*" | xargs rm -f

# ==

awk 'END {print NR}' filename

awk -F, '{print $1, $2}' filename