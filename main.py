import sys
from GeekBrains.File_Manager.core import create_file, create_folder, get_list, delete_file, copy_file, save_info, change_dir, game

save_info('Start')
try:
    command = sys.argv[1]
except IndexError:
    print('Необходимо ввести команду. Список команд вызывается командой "help"')
else:
    if command == 'list':
        get_list()
    elif command == 'create_file':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Не введено имя файла')
        else:
            create_file(name)
    elif command == 'create_folder':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Не введено имя папки')
        else:
            create_folder(name)
    elif command == 'delete':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Не указано имя файла')
        else:
            delete_file(name)
    elif command == 'copy':
        try:
            name = sys.argv[2]
            new_name = sys.argv[3]
        except IndexError:
            print('Не указаны имя копируемой и новой папки')
        else:
            copy_file(name, new_name)
    elif command == 'help':
        print('list - список файлов и папок')
        print('create_file - создание файла')
        print('create_folder - создание папки')
        print('delete - удаление файла')
        print('copy - копирование файла')
        print('change_dir - смена папки')
        print('game - давай сыграем')
    elif command == 'change_dir':
        try:
            path = sys.argv[2]
        except IndexError:
            print('Не указана директория')
        else:
            change_dir(path)
    elif command == 'game':
        game()
    save_info('Finish')
