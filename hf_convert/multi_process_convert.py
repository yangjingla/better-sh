import os
import json
import glob
from tqdm import tqdm
import time
from multiprocessing import Pool


def load_jsonl_file(file):

    BAR_INFO = "[pid={}]".format(os.getpid())
    data = []
    with open(file, "r") as f:
        for line in tqdm.tqdm(f.readlines(), desc=BAR_INFO):
            data.append(json.loads(line))

    return data
        


def write_jsonl_file(filname):
    BAR_INFO = "[pid={}]".format(os.getpid())

    with open(filename, "w") as f:
        f.write(fmt + "\n")
        for line in tqdm(range(100), desc=BAR_INFO):
            fmt = "This is {} line!!".format(line)
            f.write(fmt + "\n")


def file_path_list(dir):
    """ 
        遍历文件夹下以 [FILE_SUFFIX] 结尾的函数
    """
    files = []
    FILE_SUFFIX = "jsonl"
    for path, _, file_list in os.walk(dir):
        for file in file_list:
            if file.endswith(FILE_SUFFIX):
                files.append(os.path.join(path, file))
            
    fmt = "[{}] total [{}] file ".format(dir, len(files))
    print(fmt)
    return files


def func(file, tag):
    """ 
        多进程核心处理逻辑函数
    """
    PORC_NUM = 100
    BAR_INFO = "[{}/{}][pid:{}][file:{}]".format(tag, PORC_NUM, os.getpid(), file)

    with open(file, "r") as f:

        for line in tqdm(f.readlines(), desc=BAR_INFO):
            time.sleep(0.1)



if __name__ == "__main__":

    base_dir = "test"

    files = file_path_list(base_dir)

    # 多进程
    with Pool(100) as pool:
        res = pool.starmap(func, [(file, i) for i, file in enumerate(files)])
