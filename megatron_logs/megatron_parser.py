import os
import re
from loguru import logger

from logger_parser import LoggerParser
from utils import is_valid_megatron_log_line, is_valid_torchrun_cmd


class MegatronLoggerParser(LoggerParser):

    def __init__(self, file):
        super().__init__(file)

        self.file = file
        self.megatron_logs = []
        self.torchrun_cmd = None

        #
        self.clean_log_elements()

    def report_torchrun_cmd(self):
        if not self.torchrun_cmd:
            fmt = "Not Found torchrun cmd in logfile"
            logger.error(fmt)
            return

        elements = []
        for key_value in self.torchrun_cmd.split("--"):
            elements.append(key_value.strip())
        elements.sort()
        for key_value in elements:
            if "torchrun" in key_value:
                fmt = "{}\n========".format(key_value)
            else:
                fmt = "\t--{}".format(key_value)
            print(fmt)

    def report_valid_logs(self):

        for line in self.megatron_logs:
            print(line)

    def show(self, key):
        pass

    def save(self, key):
        pass


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


if __name__ == "__main__":

    log_file = "./logs/megatron.log"
    logparser = MegatronLoggerParser(log_file)

    # logparser.report_torchrun_cmd()
    # logparser.report_valid_logs()

    valid_log_line = " iteration      224/  158945 | consumed samples:       344064 | elapsed time per iteration (ms): 21758.0 | learning rate: 2.819E-04 | global batch size:  1536 | lm loss: 5.119438E+00 | loss scale: 1.0 | grad norm: 1.455 | number of skipped iterations:   0 | number of nan iterations:   0 | samples per second: 70.595 | TFLOPs (Hardware): 95.96 | TFLOPs (Model): 95.96 | TFLOPs GPU (Hardware): 110.49 | TFLOPs GPU (Model): 110.49 |"

    parser_elements(valid_log_line)
