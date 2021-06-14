"""3. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
Решение покрыть тестами (опционально)."""

from pathlib import Path
path = Path(__file__).resolve().parent
file_path = path / "new_file.txt"
file_path_new = path / "new_new_file.txt"

# with open(file_path, "w") as f:
#     f.write('One - 1\nTwo - 2\nThree - 3\nFour - 4')

zamena = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'} # Нужно еще настроить перевод на UTF8
result = []

with open(file_path, "r") as f:
    for line in f:
        x = line.split(" - ")
        if x[0] in zamena:
            word = zamena[x[0]]
            result.append(word + " - " + x[1])
    print(result)
f.close()


with open(file_path_new, "w") as f:
    f.writelines(result)
    f.close

