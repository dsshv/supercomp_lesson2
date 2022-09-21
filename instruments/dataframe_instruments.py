import pandas as pd
import numpy as np


def get_dataframe_from_file(filename: str, skip_before: int = 0, skip_after: int = 0):
    file = open(f'{filename}', 'r+')
    lines = file.readlines()
    file.close()

    for i in range(skip_before):
        lines.remove(lines[0])
    for i in range(skip_after):
        lines.remove(lines[-1])

    for i in range(len(lines)):
        split_line = lines[i].split('  ')
        lines[i] = split_line[1::]

    lines_list = np.array(lines, np.float)
    data = pd.DataFrame(lines_list)

    return data
