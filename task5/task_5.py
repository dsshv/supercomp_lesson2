from classes.directory import Directory
from classes.pdf import Pdf
from utils.dataframe_utils import get_dataframe_from_file

LESSON_DIR = '/home/student/Polozhentsev/data/'
VALID_FOLDERS_NAMES = ['DLS', 'TEM', 'UV-vis', 'XEOL', 'XRD']
TASK_DIR = './task5/downloaded_dirs/'
FULL_TASK_DIR = '/home/dsshv/PycharmProjects/supercoputers_software/task5/'

def task_main():
    # file_1 = '/home/dsshv/PycharmProjects/supercoputers_software/task5/downloaded_dirs/UV-vis/UV-vis_acetone.txt'
    # file_2 = '/home/dsshv/PycharmProjects/supercoputers_software/task5/downloaded_dirs/XEOL' \
    #          '/73_XEOL_P1_GdF3_Tb5_35kV_16mA.txt '
    # file_3 = '/home/dsshv/PycharmProjects/supercoputers_software/task5/downloaded_dirs/XRD/005' \
    #          '-1_XRD_P1_GdF3_Tbx5_NH4F_water_RT_exported.xy'
    # df = get_dataframe_from_file(file_3, skip_before=1, sep=' ')
    # df = get_dataframe_from_file(file_2, skip_before=2, skip_after=244, sep=' ')
    # print(df)

    input_dir = input('Input folder name. Leave it empty to parse all folders')
    while not input_dir in VALID_FOLDERS_NAMES:
        print('invalid folder name :(\n'
              'Allowed folder names: \n')
        for name in VALID_FOLDERS_NAMES:
            print(name)
        input_dir = input('Input folder name. Leave it empty to parse all folders')

    parsed_dir = Directory(f'{LESSON_DIR}{input_dir}/')
    parsed_dir.ls()

    downloaded_dir = parsed_dir.download_dir(f'{TASK_DIR}{input_dir}/')
    paths = downloaded_dir.get_full_records_paths()
    pdf = Pdf(paths, FULL_TASK_DIR)
    pdf.create_pdf()
    #print(paths)
    # # print(f'***\n'
    # #       f'{LESSON_DIR}{input_dir}\n'
    # #       f'{TASK_DIR}{input_dir}/\n'
    # #       f'***')
