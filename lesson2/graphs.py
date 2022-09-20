import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def get_dataframe_from_file(filename: str, skipped_strings: int = 0):
    file = open(f'{filename}', 'r+')
    lines = file.readlines()

    for i in range(skipped_strings):
        lines.remove(lines[0])

    for i in range(len(lines)):
        split_line = lines[i].split('  ')
        lines[i] = split_line[1::]

    lines_list = np.array(lines, np.float)
    data = pd.DataFrame(lines_list)

    return data


