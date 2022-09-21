import paramiko


class Connection:

    def __init__(self, hostname, username, password):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.connection = self.set_ssh_connection

    def set_ssh_connection(self):
        ssh_connection = paramiko.SSHClient()
        ssh_connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_connection.connect(
            hostname=self.hostname,
            username=self.username,
            password=self.password
        )
        return ssh_connection

    def sftp_put_many(self, files: list, path: str):
        sftp = self.connection.open_sftp()
        for file in files:
            place_to_upload = f'{path}/{file}'
            sftp.put(file, place_to_upload)
        sftp.close()

    def sftp_get_many(self, files: list, path: str):
        sftp = self.connection.open_sftp()
        for file in files:
            place_to_save = f'{path}/file'
            sftp.get(file, place_to_save)
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
