def read_file(path):
    try:
        with open(path, mode="r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print("Ошибка: файл не найден")
    except PermissionError:
        print("Ошибка: нет прав доступа")
    except UnicodeDecodeError:
        print("Ошибка: невозможно прочитать файл")
    except OSError as e:
        print(f"Ошибка операционной системы: {e}")
    return None
path = input("Путь к файлу: ")
content = read_file(path)

if content is not None:
    print(content)