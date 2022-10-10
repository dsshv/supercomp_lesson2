from utils.dataframe_utils import get_dataframe_from_file

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
        # plt.show()

        dataframe2 = dataframe
        min_y = dataframe2['<xanes>'].min()
        dataframe2['<xanes>'] -= min_y
        max_y = dataframe2['<xanes>'].max()
        dataframe2['<xanes>'] /= max_y
        plt.plot(dataframe2['Energy'], dataframe2['<xanes>'])
        # plt.show()

        dataframe3 = dataframe2
        dataframe3['<xanes>'] += 1
        plt.plot(dataframe3['Energy'], dataframe3['<xanes>'])

        dataframe4 = dataframe2
        dataframe4['<xanes>'] += 1
        plt.plot(dataframe4['Energy'], dataframe4['<xanes>'])
        # plt.show()

        dataframe5 = dataframe2
        dataframe5['<xanes>'] += 1
        plt.plot(dataframe5['Energy'], dataframe5['<xanes>'])
        plt.show()

    normalize_task()
    # graph_task()
