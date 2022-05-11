

def vonNeumann(FileNameIn: str, FileNameOut: str = "OutData"):
    print(f"Начало работы программы открываем файл {FileNameIn}.txt\nПожалуйста, ожидайте")
    outbuf = ''
    with(open(FileNameIn + ".txt", "r")) as file:
        lines = file.readlines()
        # Файл имеет одну строку?
        if len(lines) == 1:
            # Проверяем, что файл имеет только 0 и 1
            _ = set(lines[0])
            print(f'Длинна полученных данных: {len(lines[0])}')
            if '0' in _ and '1' in _ and len(_) == 2:
                for i in range(0, len(lines[0]), 2):
                    if lines[0][i] == "1" and lines[0][i+1] == "0":
                        outbuf += '1'
                    elif lines[0][i] == "0" and lines[0][i+1] == "1":
                        outbuf += '0'
                    else:
                        # Текущее состояние не требует добавления
                        pass
            else:
                print("Неверный формат файла. Присутствуют значения кроме 0 и 1")
        else:
            print("Неверный формат файла. Больше одной строки")
            return 1

    with(open(FileNameOut + '.txt', 'w')) as fileout:
        fileout.write(outbuf)
    print(f'Длинна выходных данных: {len(outbuf)}')
    print(f"Программа завершена.Создан файл с именем {FileNameOut}.txt")




if __name__ == '__main__':

    fileNameIn = "txtData"

    vonNeumann(fileNameIn)
