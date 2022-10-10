from classes.ssh_connection import Connection
from config import SERVER_HOSTNAME, SERVER_PASSWORD, SERVER_USERNAME
from enum import Enum
from os import listdir


class AccessTypes(Enum):
    server = 'server'
    local = 'local'


class Directory:

    def __init__(self, path: str, access_type: AccessTypes = AccessTypes.server.value):
        self.path = path
        self.access_type = access_type
        # print(self.access_type)
        if access_type == 'server':
            self.records = self.__ssh_parse_dir()
        else:
            self.records = self.__parse_dir()

    def download_dir(self, path_to_save: str):
        if self.access_type == 'local':
            print('There is no way to download file from local host')
            return

        downloadable_records = []
        for record in self.records:
            file = f'{self.path}{record}'
            downloadable_records.append(file)

        srv = Connection(SERVER_HOSTNAME, SERVER_USERNAME, SERVER_PASSWORD)
        srv.sftp_get(downloadable_records, path_to_save)
        srv.connection.close()
        # self.access_type = AccessTypes.local.value
        # self.path = path_to_save
        return Directory(path_to_save, AccessTypes.local.value)

    def get_full_records_paths(self):
        paths = []
        for record in self.records:
            p = self.path + record
            # print(self.path, record)
            paths.append(p)
        return paths

    def __ssh_parse_dir(self):
        srv = Connection(SERVER_HOSTNAME, SERVER_USERNAME, SERVER_PASSWORD)
        ls = srv.exec(f'ls {self.path}', False)
        srv.connection.close()
        if not ls:
            print('unexpected error')
            return
        for i in range(len(ls)):
            ls[i] = ls[i].replace('\n', '')
            #ls[i] = file[:-1]
        return ls

    def __parse_dir(self):
        ls = listdir(self.path)
        return ls

    def ls(self):
        print(self.records)
