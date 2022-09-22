from instruments.dataframe_instruments import get_dataframe_from_file
import pandas as pd


def lesson_2():

    def graph_task():
        text_file = './input_files/out.txt'
        dataframe = get_dataframe_from_file(text_file, 2)
