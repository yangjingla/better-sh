
# set -x
# ===


hostfile=$1
user=root
nodes=$(awk 'END {print NR}'  "$hostfile")


cmds=(
    "npu-smi info"
    "docker ps"
    "cat /etc/os-release"
)


for ip in $(cat  "$hostfile")
do
    echo  -e "ip=${ip}"
    for cmd in "${cmds[@]}"
    do
        echo -e "\t>${cmd}"
        # ssh user@${ip} ${cmd}
    done
done

fmt="summary:\n\t>Total [${nodes}] Nodes in [$(readlink -f "$hostfile")]"
echo -e ${fmt}