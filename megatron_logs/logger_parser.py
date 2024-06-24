import json
import re
import os
from loguru import logger
from utils import is_valid_megatron_log_line, is_valid_torchrun_cmd


class LoggerParser:
    """ """

    def __init__(self, file):
        self.log_file_path = file

        self.torchrun_cmd = None
        self.megatron_logs = []

    def clean_log_elements(self):
        with open(self.log_file_path, "r") as f:
            for line in f.readlines():
                valid_cmd_flag = is_valid_torchrun_cmd(line)
                if valid_cmd_flag:
                    self.torchrun_cmd = line

                valid_flag = is_valid_megatron_log_line(line)
                if valid_flag:
                    self.megatron_logs.append(line)

    def parser_elements(valid_log_line):

        iteration_pattern = r" iteration\s+(\d+)/\s+(\d+)\s+\|"
        elements_pattern = r"\| (\w+[^:]*):[ ]*([\d\.E\+]+) \|"

        elements_matches = re.findall(elements_pattern, valid_log_line)
        iteration_matches = re.findall(iteration_pattern, valid_log_line)

        extracted_elements = {}
        extracted_elements["iteration"] = eval(iteration_matches[0][0])
        extracted_elements["total_iteration"] = eval(iteration_matches[0][1])

        for key, value in elements_matches:
            extracted_elements[key] = eval(value)

        for key, value in extracted_elements.items():
            print(f"{key}: {value}")

        return extracted_elements

    def get_args(self):
        pass

    def get_lr(self):
        pass

    def get_loss(self):
        pass

    def get_troughtout(self):
        pass

    def get_mfu(self):
        pass
