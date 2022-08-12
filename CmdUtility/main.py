from APIWorker import APIWorker
from Menu import Menu


def main():
    api_worker = APIWorker()
    menu = Menu(api_worker)

    menu.processing()


if __name__ == '__main__':
    main()