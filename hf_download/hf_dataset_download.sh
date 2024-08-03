
# ==
# https://huggingface.co/docs/huggingface_hub/guides/cli#huggingface-cli-download
# pip install -U huggingface_hub[hf_transfer]
# ==

export HF_ENDPOINT=https://hf-mirror.com
export HF_HUB_DOWNLOAD_TIMEOUT=30
DIR=${pwd}


DATASETS=(

)
ALLOW_PATTERNS="" #"*.parquet"


for DATASET_ID in "${DATASETS[@]}"
do

    LOCAL_DIR=${DIR}/${DATASET_ID}

    if [ ! -d ${LOCAL_DIR} ]
    then
        mkdir -p ${LOCAL_DIR}
    fi

    huggingface-cli download ${DATASET_ID} --repo-type dataset --local-dir ${LOCAL_DIR} --include ${ALLOW_PATTERNS} --exclude  ${EXCLUDE}
done