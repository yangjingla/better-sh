
# ==
# https://huggingface.co/docs/huggingface_hub/guides/cli#huggingface-cli-download
pip install huggingface_hub[hf_transfer]


export HF_HUB_DOWNLOAD_TIMEOUT=30


MODEL_ID=AI-ModelScope/gpt2
ALLOW_PATTERNS="*.safetensors"
EXCLUDE="*.fp16.*"*
LOCAL_DIR=/Users/yangjing/Desktop/RD/better-sh/hf_download/${MODEL_ID}


set -x
# ==
huggingface-cli download ${MODEL_ID} --local-dir ${LOCAL_DIR}  --include ${ALLOW_PATTERNS} --exclude  ${EXCLUDE}



# huggingface-cli download HuggingFaceH4/ultrachat_200k --repo-type dataset