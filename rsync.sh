

exclude_folders=(
    "bash*"
    "hostfile"
)


exclude_options=""
for folder in "${exclude_folders[@]}"; do
    exclude_options+=" --exclude=$folder"
done


#
source_dir=/Users/yangjing/Desktop/RD/vllm
target_dir=/Users/yangjing/Desktop/test
mkdir -p ${target_dir}



cmd="rsync -av  ${exclude_options} ${source_dir} ${target_dir}"
echo ${cmd}
eval ${cmd}


