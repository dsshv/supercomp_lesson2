import paramiko
import os
import lesson2.graphs as l2

SERVER_DIR = '/home/student/Students/Shevtsov/lesson2/'
HOME_DIR = '/home/dsshv/PycharmProjects/supercoputers_software/'

FDM_DIR = '/home/student/Students/Shevtsov/lesson2/fdmdir/'
FDM_FILE = '/home/dsshv/PycharmProjects/supercoputers_software/fdmfile.txt'
IN_FILE = '/home/dsshv/PycharmProjects/supercoputers_software/in.txt'


def sftp_connection_op(ssh_connection):
    sftp = ssh_connection.open_sftp()
    file_to_upload = './test.txt'
    file_to_download = f'{SERVER_DIR}test2.txt'
    place_to_save = 'test2.txt'
    sftp.put(file_to_upload, f'{SERVER_DIR}/text.txt')
    sftp.get(file_to_download, place_to_save)

    sftp.put(file_to_upload, f'{SERVER_DIR}/text3.txt')
    sftp.put(file_to_upload, f'{SERVER_DIR}/text4.txt')

    sftp.remove(f'{SERVER_DIR}/text3.txt')
    sftp.remove(f'{SERVER_DIR}/text5.txt')
    sftp.rename(f'{SERVER_DIR}/text4.txt', f'{SERVER_DIR}/text5.txt')

    print('sftp op done')
    sftp.close()


def os_op(ssh_connection):
    stdin, stdout, stderr = ssh_connection.exec_command(f'ls {SERVER_DIR}')
    ls_dir = stdout.readlines()
    print(ls_dir)
    ssh_connection.exec_command(f'cd {SERVER_DIR}')
    stdin, stdout, stderr = ssh_connection.exec_command(f'ls -> files_list_in_this_dir.txt')
    list_files = stdout.readlines()


def run_cluster(ssh_connection):
    sftp = ssh_connection.open_sftp()
    # sftp.mkdir(FDM_DIR)
    sftp.put(FDM_FILE, f'{FDM_DIR}/fdmfile.txt')
    sftp.put(IN_FILE, f'{FDM_DIR}/in.txt')

    stdin, stdout, stderr = ssh_connection.exec_command(f'cd {FDM_DIR};'
                                                        f' run-cluster fdmnes -n 1 -j SHEVTSOV -e dshevtsov@sfedu.ru')

    li = stdout.readlines()
    if (stderr):
        error = stderr.readlines()
        print(error)
    sftp.close()


def get_fdm(ssh_connection):
    sftp = ssh_connection.open_sftp()
    sftp.get(f'{FDM_DIR}out.txt', 'out.txt')
    sftp.close()


def copy_and_edit_files(ssh_connection):
    file_names = ['in-2.txt', 'in-3.txt', 'in-4.txt']

    with open(f'./in.txt', 'r+') as file:
        all_lines = file.readlines()

        for name in file_names:
            new_string = ''
            line_to_edit = all_lines[15].split(' ')

            for value in line_to_edit:

                if value == '\n':
                    break

                new_value = str(
                    float(value) + 2
                )
                new_string += new_value + ' '

            all_lines[15] = new_string + '\n'

            with open(f'./{name}', 'w') as new_file:
                new_file.writelines(all_lines)
                new_file.close()
    file.close()

    file = open(f'./fdmfile.txt', 'r+')
    lines = file.readlines()

    for name in file_names:
        lines.append(name + '\n')
    lines[0] = str(
        len(file_names) + 1
    ) + '\n'
    file.close()

    file = open(f'./fdmfile.txt', 'w')
    file.writelines(lines)
    file.close()

    sftp = ssh_connection.open_sftp()
    # sftp.mkdir(FDM_DIR)
    sftp.put(FDM_FILE, f'{FDM_DIR}/fdmfile.txt')
    sftp.put(IN_FILE, f'{FDM_DIR}/in.txt')
    sftp.put(IN_FILE, f'{FDM_DIR}/in-2.txt')
    sftp.put(IN_FILE, f'{FDM_DIR}/in-3.txt')
    sftp.put(IN_FILE, f'{FDM_DIR}/in-4.txt')
    stdin, stdout, stderr = ssh_connection.exec_command(f'cd {FDM_DIR};'
                                                        f' run-cluster fdmnes -n 1 -j SHEVTSOV -e dshevtsov@sfedu.ru')
    sftp.close()







if __name__ == '__main__':
    ssh = set_ssh_connection()
    #sftp_connection_op(ssh)
    #os_op(ssh)
    #run_cluster(ssh)
    #get_fdm(ssh)
    #copy_and_edit_files(ssh)
    ssh.close()
    data = l2.get_dataframe_from_file('out.txt', 2)
    print(data)
