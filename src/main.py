from operations import read_file, write_to_file


def main():
    route = input("Введите путь к файлу: ")
    data = read_file(route)
    write_to_file(data)


if __name__ == "__main__":
    main()
