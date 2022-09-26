import altair

from instruments.dataframe_instruments import get_dataframe_from_file
import pandas as pd
import altair as alt
import seaborn as sns

import matplotlib.pyplot as plt


def lesson_2():
    def graph_task():
        text_file = './lesson2/input_files/out.txt'
        dataframe = get_dataframe_from_file(text_file, 2)
        dataframe.rename(
            columns={0: 'Energy', 1: '<xanes>'},
            inplace=True
        )
        print(dataframe)

        plt.plot(dataframe['Energy'], dataframe['<xanes>'])
        plt.show()

    def normalize_task():
        text_file = './lesson2/input_files/out.txt'
        dataframe = get_dataframe_from_file(text_file, 2)
        dataframe.rename(
            columns={0: 'Energy', 1: '<xanes>'},
            inplace=True
        )
        plt.plot(dataframe['Energy'], dataframe['<xanes>'])
        plt.show()

        min_y = dataframe['<xanes>'].min()
        dataframe['<xanes>'] -= min_y
        max_y = dataframe['<xanes>'].max()
        dataframe['<xanes>'] /= max_y

        plt.plot(dataframe['Energy'], dataframe['<xanes>'])
        plt.show()

    normalize_task()
    # graph_task()
