
# ==
# https://huggingface.co/docs/huggingface_hub/guides/cli#huggingface-cli-download
# pip install -U huggingface_hub[hf_transfer]
# ==


export HF_HUB_DOWNLOAD_TIMEOUT=30

# ==
# 下载模型
# ==
MODEL_ID=
ALLOW_PATTERNS="*.bin"
EXCLUDE="*.fp16.*"*
LOCAL_DIR=/Users/yangjing/Desktop/RD/better-sh/hf_download/${MODEL_ID}

set -x
# ==
# huggingface-cli download ${MODEL_ID} --local-dir ${LOCAL_DIR}  --include ${ALLOW_PATTERNS} --exclude  ${EXCLUDE}

# ==
# 下载数据
# ==
DATASET_ID=tatsu-lab/alpaca
ALLOW_PATTERNS="*.parquet"
LOCAL_DIR=/Users/yangjing/Desktop/RD/better-sh/hf_download/${DATASET_ID}

huggingface-cli download ${DATASET_ID} --repo-type dataset --local-dir ${LOCAL_DIR} --include ${ALLOW_PATTERNS} --exclude  ${EXCLUDE}