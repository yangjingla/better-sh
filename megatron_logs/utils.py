import re


MEGATRON_KEYS = [
    " iteration ",
    " consumed samples",
    " elapsed time per iteration",
    " learning rate",
    " global batch size",
    " loss scale",
    " grad norm",
]

TORCHRUN_KEYS = ["torchrun", "--nproc_per_node", "--nnodes", "--master_addr"]


def is_valid_megatron_log_line(line):
    valid = True
    for key in MEGATRON_KEYS:
        if key not in line:
            valid = False
            break

    return valid


def is_valid_torchrun_cmd(line):
    valid = True
    for key in TORCHRUN_KEYS:
        if key not in line:
            valid = False
            break

    return valid


def parser_argument(file):
    pass
