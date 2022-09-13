import paramiko
import os

SERVER_DIR = '/home/student/Students/Shevtsov/lesson2/'
HOME_DIR = '/home/dsshv/PycharmProjects/supercomp_lesson2/'


def set_ssh_connection():
    ssh_connection = paramiko.SSHClient()
    ssh_connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_connection.connect(
        hostname='195.208.250.3',
        username='student',
        password='Xanes2000'
    )
    return ssh_connection


def sftp_connection_op(ssh_connection):
    sftp = ssh_connection.open_sftp()
    cwd = os.getcwd()
    files = os.listdir(cwd)
    print(files)
    ssh_connection.exec_command(f'cd ./{SERVER_DIR}')
    file_to_upload = './test.txt'
    file_to_download = f'{SERVER_DIR}test2.txt'
    place_to_save = 'test2.txt'
    sftp.put(file_to_upload, f'{SERVER_DIR}/text.txt')
    sftp.get(file_to_download, place_to_save)

    sftp.put(file_to_upload, f'{SERVER_DIR}/text3.txt')
    sftp.put(file_to_upload, f'{SERVER_DIR}/text4.txt')
    sftp.remove(f'{SERVER_DIR}/text3.txt')
    sftp.rename(f'{SERVER_DIR}/text4.txt', f'{SERVER_DIR}/text5.txt')

    sftp.mkdir(f'{SERVER_DIR}/new_dir/')

    print('sftp op done')
    sftp.close()


def os_op(ssh_connection):
    stdin, stdout, stderr = ssh_connection.exec_command(f'ls {SERVER_DIR}')
    ls_dir = stdout.readlines()
    print(ls_dir)
    ssh_connection.exec_command(f'cd ./{SERVER_DIR}')
    stdin, stdout, stderr = ssh_connection.exec_command(f'ls -> files_list_in_this_dir.txt')
    list_files = stdout.readlines()
    print(list_files)


if __name__ == '__main__':
    ssh = set_ssh_connection()
    os.chdir(HOME_DIR)
    sftp = ssh.open_sftp()
    sftp_connection_op(ssh)
    os_op(ssh)
    ssh.close()
