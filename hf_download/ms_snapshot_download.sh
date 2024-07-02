

# ==
# pip install -U modelscope
# pip install -U opencv-python
set -x

pip install -U huggingface_hub  #huggingface_hub==0.23.4

DIR=${PWD}
MODEL_ID=AI-ModelScope/gpt2
ALLOW_PATTERNS='*.json'
LOCAL_DIR=${PWD}/${MODEL_ID}

mkdir -p ${LOCAL_DIR}


modelscope download --model ${MODEL_ID} --include ${ALLOW_PATTERNS} --local_dir ${LOCAL_DIR}