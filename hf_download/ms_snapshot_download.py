import os
import sys
from loguru import logger
import subprocess


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


try:
    from modelscope import snapshot_download
except ImportError:
    logger.warning("install [modelscope]..")
    install("modelscope")
    from modelscope import snapshot_download
    


def set_proxies():
    pass


MODEL_ID = "AI-ModelScope/phi-2"
LOCAL_DIR = "/Users/yangjing/Desktop/RD/better-sh/hf_download/{}".format(MODEL_ID)
if not os.path.exists(LOCAL_DIR):
    logger.warning("create [{}]...".format(LOCAL_DIR))
    os.makedirs(LOCAL_DIR)


ALLOW_PATTERNS = ["*.md", "*.json", "*.bin", "*.py"]
IGNOR_PATTERNS = []


snapshot_download(
    model_id=MODEL_ID,
    local_dir=LOCAL_DIR,
    allow_file_pattern=ALLOW_PATTERNS,
    ignore_file_pattern=IGNOR_PATTERNS,
)
