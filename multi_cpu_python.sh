
# set -x

RANK_ID_START=0
RANK_SIZE=8

# linux
# nproc=${nproc}
# mac
nproc=$(sysctl -n hw.ncpu)

KERNEL_NUM=$(( $nproc/ 8 ))

for ((RANK_ID=${RANK_ID_START} ; RANK_ID < $(( RANK_SIZE + RANK_ID_START)); RANK_ID++ ))
do
    echo "RANK_ID= ${RANK_ID}"

    PID_START=$((KERNEL_NUM*RANK_ID ))
    PID_END=$(( PID_START + KERNEL_NUM -1))

    taskset -c $PID_START-$PID_END python test.py  & # 后台运行

done
