import os
from time import time
from APIWorker import APIWorker


class Menu:
    def __init__(self, api_worker: APIWorker):
        self.api_worker = api_worker

    def processing(self):
        while True:
            command = input('> ')
            if command == 'help':
                self.show_help()
            elif command == 'clear':
                os.system('cls')
            elif command == 'scan new':
                self.create()
            elif command.startswith('scan upd'):
                try:
                    self.update(int(command.split()[-1]))
                except ValueError:
                    print('Invalid command, retry\n')
                    continue
            elif command.startswith('scan del'):
                try:
                    self.delete(int(command.split()[-1]))
                except ValueError:
                    print('Invalid command, retry')
                    continue
            elif command.startswith('scan get'):
                try:
                    self.read(int(command.split()[-1]))
                except ValueError:
                    print('Invalid command, retry')
                    continue
            elif command == 'scan get /all':
                self.read_all()
            elif command == 'quit':
                return
            else:
                print('Invalid command, retry')
                continue


    @staticmethod
    def show_help():
        print('''
        Commands for work with the utility:
        1. scan new - creates a new scan report
        2. scan upd <key> - updates an existing scan report
        3. scan del <key> - deletes an existing scan report
        4. scan get <key> - reads an existing scan report
        5. scan get /all - reads all scan reports
        6. scan quit - quits the utility\n
        ''')

    def create(self):
        path = input('Enter the directory path: ')
        files = [path + '\\' + file for file in os.listdir(path) if self.is_file(path + '\\' + file)]
        report = self.scan_dir(path, files)
        print(report)
        response = self.api_worker.create(report)
        if response:
            print('Scan report was created successfully')
        else:
            print('Error occured while creating scan report')

    @staticmethod
    def is_file(file):
        try:
            os.listdir(file)
            return False
        except NotADirectoryError:
            return True

    @staticmethod
    def scan_dir(path, files):
        report = {
            'directory': path,
            'js_files': 0,
            'rmrf_files': 0,
            'rundll_files': 0,
            'errors': 0,
            'execution_time': 0.0,
            'is_completed': False
        }

        cnt = 0
        start_time = time()
        for file in files:
            try:
                with open(file, encoding='utf-8') as f:
                    lines = f.readlines()
            except Exception:
                report['errors'] += 1
                continue

            for line in lines:
                if '<script>evil_script()</script>' in line:
                    report['js_files'] += 1
                    break
                if 'rm -rf %userprofile%\\Documents' in line:
                    report['rmrf_files'] += 1
                    break
                if 'Rundll32 sus.dll SusEntry' in line:
                    report['rundll_files'] += 1
                    break
            cnt += 1
        end_time = time()

        float_time = end_time - start_time
        hours, seconds = divmod(float_time * 60, 3600)
        minutes, seconds = divmod(seconds, 60)
        report['execution_time'] = f'{int(hours)}:{int(minutes)}:{int(seconds)}'
        report['is_completed'] = True if cnt == len(files) else False
        return report

    def update(self, primary_key):
        report = self.api_worker.read(primary_key)
        path = report['directory']
        files = [file for file in os.listdir(path) if self.is_file(path + '\\' + file)]
        upd_report = self.scan_dir(path, files)
        response = self.api_worker.update(primary_key, upd_report)
        if response:
            print('Scan report was updated successfully')
        else:
            print('Error occured while updating scan report')

    def delete(self, primary_key):
        response = self.api_worker.delete(primary_key)
        if response:
            print('Scan report was deleted successfully')
        else:
            print('Error occured while deleting scan report')

    def read(self, primary_key):
        report = self.api_worker.read(primary_key)
        if report:
            for key, value in report.items():
                print(f'{key}: {value}')
            print('Scan report was got successfully')
        else:
            print('Error occured while getting scan report')

    def read_all(self):
        reports = self.api_worker.read_all()
        if reports:
            for report in reports:
                for key, value in report.items():
                    print(f'{key}: {value}')
            print('Scan reports were got successfully')
        else:
            print('Error occured while getting scan reports')
