from pathlib import Path

root = Path(input("Каталог: "))
ext = input("Расширение: ")

if not root.is_dir():
    print(f"Ошибка: каталог '{root}' не существует")
else:
    found = [p for p in root.rglob("*") if p.is_file() and p.suffix == ext]

    if not found:
        print(f"Файлы {ext} не найдены")
    else:
        for p in found:
            print(f"{p} - {p.stat().st_size} байт")