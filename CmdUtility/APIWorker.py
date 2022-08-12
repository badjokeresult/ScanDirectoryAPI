import requests


class APIWorker:
    @staticmethod
    def create(report):
        response = requests.post('http://127.0.0.1:8000/api/v1/scans/scan/create/', report)
        return response.ok

    @staticmethod
    def read(key):
        response = requests.get(f'http://127.0.0.1:8000/api/v1/scans/scan/detailed/{key}/')
        return response.json()

    @staticmethod
    def read_all():
        response = requests.get('http://127.0.0.1:8000/api/v1/scans/all/')
        return response.json()

    @staticmethod
    def update(key, report):
        response = requests.put(f'http://127.0.0.1:8000/api/v1/scans/scan/update/{key}/', report)
        return response.ok

    @staticmethod
    def delete(key):
        response = requests.delete(f'http://127.0.0.1:8000/api/v1/scans/scan/delete/{key}/')
        return response.ok