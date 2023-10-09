from utils import *

FILE_JSON = "../json/operations.json"


def main():
    try:
        operations_list = load_file(FILE_JSON)
        operations = make_operations(operations_list)
        print(get_executed_five(operations))
    except FileNotFoundError:
        print("Файл не найден")


if __name__ == "__main__":
    main()
