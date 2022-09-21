import paramiko


class Connection:

    def __init__(self, hostname, username, password):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.connection = paramiko.SSHClient()
        self.connection_on = self.set_ssh_connection()

    def set_ssh_connection(self):

        self.connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.connection.connect(
            hostname=self.hostname,
            username=self.username,
            password=self.password
        )
        return self.connection

    def sftp_put(self, files: list, path: str):
        sftp = self.connection.open_sftp()
        for file in files:
            file_name = file.split(sep='/')[-1]
            place_to_upload = f'{path}/{file_name}'
            sftp.put(file, place_to_upload)
        sftp.close()

    def sftp_get(self, files: list, path: str):
        sftp = self.connection.open_sftp()
        for file in files:
            file_name = file.split(sep='/')[-1]
            place_to_save = f'{path}/{file_name}'
            sftp.get(file, place_to_save)
        sftp.close()

    def sftp_remove(self, files: list):
        sftp = self.connection.open_sftp()
        for file in files:
            sftp.remove(file)
        sftp.close()

    def sftp_rename(self, file_old_name: str, file_new_name: str):
        sftp = self.connection.open_sftp()
        sftp.rename(file_old_name, file_new_name)
        sftp.close()

    def exec(self, command: str, no_output: bool = False):
        stdin, stdout, stderr = self.connection.exec_command(command)
        if stderr:
            error = stderr.readlines()
            print(error)
            return
        if no_output:
            return
        output = stdout.readlines()
        print(output)
