

# ==
# pip install -U modelscope
# pip install -U opencv-python


pip install -U huggingface_hub  #huggingface_hub==0.23.4


MODEL_ID=AI-ModelScope/gpt2
ALLOW_PATTERNS='*.json, *.bin'
LOCAL_DIR=/Users/yangjing/Desktop/RD/better-sh/hf_download/${MODEL_ID}

mkdir -p ${LOCAL_DIR}


modelscope download --model ${MODEL_ID} --include ${ALLOW_PATTERNS} --local_dir ${LOCAL_DIR}