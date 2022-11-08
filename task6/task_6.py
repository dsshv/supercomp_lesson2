from config import SERVER_DIR, HOME_DIR, SERVER_HOSTNAME, SERVER_PASSWORD, SERVER_USERNAME
from utils.dataframe_utils import get_dataframe_from_file
from classes.ssh_connection import Connection
import matplotlib.pyplot as plt

def task_main():
    PREFIX = './task6/input_files/'
    UPLOAD_DIR = './task6/output_files/'
    nodes = int(input("Number of nodes:  "))

    srv = Connection(SERVER_HOSTNAME, SERVER_USERNAME, SERVER_PASSWORD)
    place_to_upload = f'{SERVER_DIR}task6/'

    file_names = []
    for i in range(nodes):
        file_names.append(f'in-{i+1}.txt')
    
    
    with open(f'./task6/input_files/in.txt', 'r+') as file:
            all_lines = file.readlines()

            range_line = all_lines[12].split(' ')
            start = int(range_line[0])
            intervall = int(range_line[-1]) - int (range_line[0])
            part = intervall // nodes


            for i in range(len(file_names)):
                new_string = f'{start + i * part + 1} 1 {(start + i * part) + part}\n'

                all_lines[12] = new_string + '\n'

                with open(f'./task6/output_files/{file_names[i]}', 'w') as new_file:
                    new_file.writelines(all_lines)
                    new_file.close()

    file.close()

    with open(f'./task6/output_files/fdmfile.txt', 'w') as file:
        text = []
        text.append(f'{len(file_names)}\n')
        for name in file_names:
            text.append(f'{name}\n')
        file.writelines(text)
    file.close()

    files_to_upload = []
    for name in file_names: 
        files_to_upload.append(f'{UPLOAD_DIR}{name}')
    files_to_upload.append(f'{UPLOAD_DIR}fdmfile.txt')

    srv.sftp_put(files_to_upload, place_to_upload)
    srv.exec(f'cd {SERVER_DIR}task6/;'
                f'run-cluster fdmnes -n 1 -j SHEVTSOV -e dshevtsov@sfedu.ru')

    ls = srv.exec('ls ~/Students/Shevtsov/task6', print_out=False)

    max_num = 0
    for f in ls: 
        if 'slurm-' in f:
            num = int(f.replace('slurm-', '').replace('.out\n', ''))
            if num > max_num: max_num = num
    
    srv.sftp_get([f'{SERVER_DIR}task6/slurm-{max_num}.out'], f'./task6/output_files')

    with open(f'./task6/output_files/slurm-{max_num}.out', 'r+') as file:
        data = []
        all_lines = file.readlines()
        for i in range(len(all_lines)):
            line = all_lines[i]
            if 'Energy    <xanes>' in line:
                # print(all_lines[i:i+part])
                data.append(all_lines[i+1:i+part+1])
        with open(f'./task6/output_files/data.txt', 'w') as new_file:
            for item_mass in data:
                for item in item_mass:
                    new_file.write(item)
        new_file.close()
    file.close()

    dataframe = get_dataframe_from_file('./task6/output_files/data.txt')
    dataframe.rename(
            columns={0: 'Energy', 1: '<xanes>'},
            inplace=True
    )
    plt.plot(dataframe['Energy'], dataframe['<xanes>'])
    plt.show()
    print('task 6 done')