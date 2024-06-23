
hostfile=$1
user=root
nodes=$(awk 'END {print NR}'  "$hostfile") 



for ip in $(cat  "$hostfile")
do 
    echo "ip=${ip}"


    cmd="npu-smi info"

    echo -e "\t>${cmd}"


    # ssh user@${ip} ${cmd}
done

fmt="summary=\n\tTotal [${nodes}] Nodes in [$(readlink -f "$hostfile")]"
echo -e ${fmt}