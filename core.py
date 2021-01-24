import os
import shutil
import datetime


def create_file(name, text=None):
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)


def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print('Папка с таким именем уже существует')


def get_list(folders_only=False):
    result = os.listdir()
    if folders_only:
        result = [f for f in result if os.path.isdir(f)]
    print(result)


def delete_file(name):
    if os.path.isdir(name):
        os.rmdir(name)
    else:
        os.remove(name)


def copy_file(name, new_name):
    if os.path.isdir(name):
        try:
            shutil.copytree(name, new_name)
        except FileExistsError:
            print('Папка с таким именем уже существует')
    else:
        shutil.copy(name, new_name)


def save_info(message):
    current_time = datetime.datetime.now()
    result = f'{current_time} - {message}'
    with open('log.txt', 'a', encoding='utf8') as f:
        f.write(result + '\n')


def game():
    import random

    number = random.randint(1, 100)
    # print(number)
    user_number = None
    count = 0
    levels = {1: 10, 2: 5, 3: 3}
    level = int(input('Введите уровень сложности:  '))

    users = []
    users_count = int(input('Введите количество пользователей:  '))
    for i in range(users_count):
        users.append(input(f'Введите имя {i + 1} пользователя:   '))
    print('В игре участвуют:', users)

    is_winner = False
    winner_name = None

    max_count = levels[level]
    while not is_winner:
        count += 1
        if count > max_count:
            print('Проиграли все игроки! Использовано максимальное количество попыток!')
            break
        print(f'Попытка № {count}')
        for player in users:
            print(f'Ход игрока {player}')
            user_number = int(input('Введите число:   '))
            if user_number == number:
                is_winner = True
                winner_name = player
                break
            elif user_number < number:
                print('Бери Больше!')
            else:
                print('Бери меньше!')
    else:
        print(f'Бинго! {winner_name} угадал с {count} попытки!')


def change_dir(path):
    os.chdir(path)
    print(os.getcwd())


if __name__ == '__main__':
    create_file('text.dat')
    create_folder('new_f1')
    get_list(True)
    delete_file('new_f1')
    delete_file('text.dat')
    copy_file('new_f', 'new2')
    create_file('text.dat')
    copy_file('text.dat', 'text2.dat')
    save_info('Hello')
