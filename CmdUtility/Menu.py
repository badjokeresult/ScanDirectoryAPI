import json
import os
import regex as re
from time import time


class Menu:
    __options = [
        "1. Create scan task",
        "2. Update scan task",
        "3. Delete scan task",
        "4. Get scan task",
        "5. Get all scan tasks",
        "6. Quit"
    ]

    def __init__(self, api_worker):
        self.api_worker = api_worker

    def processing(self):
        while True:
            self.show_menu_options()

            try:
                option = int(input('Enter the menu option: '))
                assert option in range(1, 7)
            except ValueError:
                print('Invalid input, retry')
                self.cls()
                continue
            except AssertionError:
                print('Option is not in menu, retry')
                self.cls()
                continue

            if option == 6:
                print('Shutting down...')
                self.cls()
                return
            else:
                self.__funcs[option]()

    @staticmethod
    def show_menu_options():
        for option in Menu.__options:
            print(option)

    @staticmethod
    def cls():
        print('Press any key to continue...')
        input()
        os.system('cls')

    def create(self):
        try:
            path = self.enter_path()
        except AssertionError:
            print('Invalid path, quitting...')
            self.cls()
            return

        report = json.dumps(self.scan(path))
        is_success = self.api_worker.create(report)

        if is_success:
            print('Scan report was created and sent successfully')
        else:
            print('Error occured while creating and sending scan report')
        self.cls()

    @staticmethod
    def scan(path):
        report = {
            'directory': path,
            'js_files': 0,
            'rmrf_files': 0,
            'rundll_files': 0,
            'errors': 0,
            'execution_time': 0.0,
            'is_completed': False
        }

        files = [file for file in os.listdir(path) if Menu.is_file(path + '\\' + file)]
        cnt = 0
        start_time = time()
        for file in files:
            result = Menu.scan_file(path + '\\' + file)
            if result is not None:
                report[result] += 1
            cnt += 1
        end_time = time()

        report['execution_time'] = end_time - start_time
        report['is_completed'] = cnt == len(files)

        return report

    @staticmethod
    def is_file(file):
        try:
            os.listdir(file)
            return False
        except NotADirectoryError:
            return True

    @staticmethod
    def scan_file(file):
        try:
            with open(file, encoding='utf-8') as f:
                lines = f.readlines()
        except Exception:
            return 'errors'

        for line in lines:
            if '<script>evil_script()</script>' in line:
                return 'js_files'
            if 'rm -rf %userprofile%\\Documents' in line:
                return 'rmrf_files'
            if 'Rundll32 sus.dll SusEntry' in line:
                return 'rundll_files'
        return None

    @staticmethod
    def enter_path():
        pattern = r'\w+:\\(\w+|\\)+'
        path = input('Enter the directory absolute path: ')
        assert re.match(pattern, path)
        return path if not path.endswith('\\') else path[:-1]

    def update(self):
        pass

    def delete(self):
        pass

    def get(self):
        pass

    def get_all(self):
        pass

    __funcs = {
        1: create,
        2: update,
        3: delete,
        4: get,
        5: get_all,
    }
