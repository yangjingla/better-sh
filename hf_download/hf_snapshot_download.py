import os
from loguru import logger
import subprocess


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


try:
    from huggingface_hub import snapshot_download
except ImportError:
    logger.warning("install [huggingface_hub[hf_transfer]..")
    install("huggingface_hub[hf_transfer]")
    from huggingface_hub import snapshot_download


def set_proxies():
    pass


MODEL_ID = "openbmb/MiniCPM-2B-sft-bf16"
LOCAL_DIR = "/Users/yangjing/Desktop/RD/better-sh/hf_download/{}".format(MODEL_ID)
if not os.path.exists(LOCAL_DIR):
    logger.warning("create [{}]...".format(LOCAL_DIR))
    os.makedirs(LOCAL_DIR)


ALLOW_PATTERNS = ["*.md", "*.json", "*.bin", "*.py"]
IGNOR_PATTERNS = []


snapshot_download(
    repo_id=MODEL_ID,
    local_dir=LOCAL_DIR,
    allow_patterns=ALLOW_PATTERNS,
    ignore_patterns=IGNOR_PATTERNS,
)
