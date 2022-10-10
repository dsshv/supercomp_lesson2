from config import SERVER_DIR, HOME_DIR, SERVER_HOSTNAME, SERVER_PASSWORD, SERVER_USERNAME
from classes.ssh_connection import Connection


def lesson_1():
    srv = Connection(SERVER_HOSTNAME, SERVER_USERNAME, SERVER_PASSWORD)
    place_to_upload = f'{SERVER_DIR}lesson1/'
    PREFIX = './lesson1/input_files/'

    def sftp_connection_operations_task():
        files_to_upload = [
            f'{PREFIX}test.txt',
            f'{PREFIX}test2.txt',
            f'{PREFIX}test3.txt',
            f'{PREFIX}test4.txt'
        ]

        files_to_download = [
            f'{SERVER_DIR}lesson1/test.txt',
            f'{SERVER_DIR}lesson1/test2.txt'
        ]
        place_to_download = f'{HOME_DIR}lesson1/output_files/'

        files_to_remove = [
            f'{SERVER_DIR}lesson1/test4.txt'
        ]

        srv.sftp_put(files_to_upload, place_to_upload)
        srv.sftp_get(files_to_download, place_to_download)
        srv.sftp_remove(files_to_remove)

        print('task 1 done')

    def os_operations_task():
        srv.exec(f'ls {SERVER_DIR}lesson1/')
        srv.exec(f'cd {SERVER_DIR}lesson1/')
        srv.exec('ls -> files_in_lesson_dir.txt')
        srv.exec('cat files_in_lesson_dir.txt')

        print('task 2 done')

    def run_cluster_task():
        files_to_upload = [
            f'{PREFIX}fdmfile.txt',
            f'{PREFIX}in.txt'
        ]
        srv.sftp_put(files_to_upload, place_to_upload)
        srv.exec(f'cd {SERVER_DIR}lesson1/;'
                 f'run-cluster run-cluster fdmnes -n 1 -j SHEVTSOV -e dshevtsov@sfedu.ru')

        print('task 3 done')

    def get_out_file_task():
        file_to_download = [f'{SERVER_DIR}lesson1/out.txt']
        place_to_save = f'{HOME_DIR}lesson1/output_files/'
        srv.sftp_get(file_to_download, place_to_save)

        print('task 4 done')

    def copy_adn_edit_files_task():

        file_names = [
            'in-2.txt',
            'in-3.txt',
            'in-4.txt'
        ]

        #
        #   Edition of input file
        #
        with open(f'lesson1/input_files/in.txt', 'r+') as file:
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

                with open(f'./lesson1/output_files/{name}', 'w') as new_file:
                    new_file.writelines(all_lines)
                    new_file.close()
        file.close()

        #
        #   Edition of fdmnes file
        #

        file = open(f'lesson1/input_files/fdmfile.txt', 'r+')
        lines = file.readlines()

        for name in file_names:
            lines.append(name + '\n')
        lines[0] = str(
            len(file_names) + 1
        ) + '\n'
        file.close()

        file = open(f'lesson1/input_files/fdmfile.txt', 'w')
        file.writelines(lines)
        file.close()

        #
        #   Upload files on server
        #
        files_to_upload = [
            f'{PREFIX}in.txt',
            f'{PREFIX}in-2.txt',
            f'{PREFIX}in-3.txt',
            f'{PREFIX}in-4.txt',
            f'{PREFIX}fdmfile.txt'
        ]
        srv.sftp_put(files_to_upload, place_to_upload)
        srv.exec(f'cd {SERVER_DIR}lesson1/;'
                 f'run-cluster run-cluster fdmnes -n 1 -j SHEVTSOV -e dshevtsov@sfedu.ru')

        print('task 5 done')

    sftp_connection_operations_task()
    os_operations_task()
    run_cluster_task()
    get_out_file_task()
    copy_adn_edit_files_task()
