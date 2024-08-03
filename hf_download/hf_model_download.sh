
# ==
# https://huggingface.co/docs/huggingface_hub/guides/cli#huggingface-cli-download
# pip install -U huggingface_hub[hf_transfer]
# ==

export HF_ENDPOINT=https://hf-mirror.com
export HF_HUB_DOWNLOAD_TIMEOUT=30
DIR=${PWD}

MODELS=(
    "google/gemma-2-2b"
)
ALLOW_PATTERNS="" #"*.bin"
EXCLUDE="" #"*.fp16.*"*


for MODEL_ID in "${MODELS[@]}"
do
    LOCAL_DIR=${DIR}/${MODEL_ID}
    if [ ! -d ${LOCAL_DIR} ]
    then
        mkdir -p ${LOCAL_DIR}
    fi

    set -x
    huggingface-cli download ${MODEL_ID} --local-dir ${LOCAL_DIR}  --token=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
    
    # --token=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
    # --quiet 
    # --include ${ALLOW_PATTERNS} --exclude  ${EXCLUDE}

done

