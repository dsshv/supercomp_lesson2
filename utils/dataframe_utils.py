import pandas as pd
import numpy as np


def get_dataframe_from_file(filename: str,
                            sep: str = ' ',
                            skip_before: int = 0,
                            skip_after: int = 0,
                            split: bool = False):
    file = open(f'{filename}', 'r+')
    lines = file.readlines()
    file.close()

    for i in range(skip_before):
        lines.remove(lines[0])
    for i in range(skip_after):
        lines.remove(lines[-1])

    for i in range(len(lines)):
        is_spaces = lines[i].find(' ')
        if is_spaces == -1:
            split_line = lines[i].split(sep)
            for l in range(len(split_line)):
                replacer = split_line[l].replace(',', '.')
                split_line[l] = replacer
            lines[i] = split_line
            print('box 1: ', lines)
        else:
            line = lines[i].replace(',', '.').replace('\n', '')
            split_line = line.split(sep)
            print(split_line)
            if split:
                lines[i] = split_line[1::]
            else:
                lines[i] = split_line
            # print('box 2: ', lines)

    # print(lines)
    lines_list = np.array(lines, np.float)
    data = pd.DataFrame(lines_list)

    return data
