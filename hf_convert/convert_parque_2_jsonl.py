import json
from loguru import logger
from tqdm import tqdm


import pandas as pd
import pyarrow.parquet as pq
from fastparquet import ParquetFile


def process_file(file):
    pass


def save_jsonl(data, file):

    with open(file, "w", encoding="utf-8") as f:
        for line in tqdm(data, desc="save:"):
            fmt = json.dumps(line, ensure_ascii=False)
            f.write(fmt)


def load_parquet(file):

    pf = ParquetFile(file)
    data = pf.to_pandas()

    for idx, row in data.iterrows():
        fmt = "{}".format(json.dumps(row.to_json(orient="columns"), indent=2))
        breakpoint()
        print(fmt)
    # pass


def main():
    parquet_file = "/Users/yangjing/Desktop/RD/better-sh/hf_download/tatsu-lab/alpaca/data/train-00000-of-00001-a09b74b3ef9c3b56.parquet"

    load_parquet(parquet_file)


if __name__ == "__main__":
    main()
