import os.path
import csv
import wiew

def export_data():
    if not os.path.exists('data.csv'):
        with open('data.csv', 'w', encoding='utf-8') as dt:
            writer = csv.writer(dt, delimiter=';')
            writer.writerow(('surname', 'name', 'Phone', 'departament'))
    exit = ''
    while exit != 'q':
        users_data = [
            [input('введите фамилию: '), input('введите имя: '), input('введите номер телефона: '),
             input('введите отдел: ')]
        ]

        with open('data.csv', 'a', encoding='utf-8') as dt:
            writer = csv.writer(dt, delimiter=';')
            writer.writerows(
                users_data
            )

        exit = input('Для завершения ввода данных нажмите "q"\nДля продолжения нажмите "Enter"\n')

def find_surname(surname):
    if os.path.exists('data.csv'):
        with open('data.csv', 'r', encoding='utf-8') as dt:
            reader = csv.reader(dt)
            sum_list = []
            for row in reader:
                if len(row) != 0:
                    sum_list.append(row[0].split(';'))
            count = 0
            for item in sum_list:
                if surname == item[0]:
                    wiew.answer(item)
                    count += 1
            if count == 0:
                wiew.answer(f'{surname} не найден!')
    else:
        wiew.answer('Файл не найден!')


def find_name(name):
    if os.path.exists('data.csv'):
        with open('data.csv', 'r', encoding='utf-8') as dt:
            reader = csv.reader(dt)
            sum_list = []
            for row in reader:
                if len(row) != 0:
                    sum_list.append(row[0].split(';'))
            count = 0
            for item in sum_list:
                if name == item[1]:
                    wiew.answer(item)
                    count += 1
            if count == 0:
                wiew.answer(f'{name} не найден!')
    else:
        wiew.answer('Файл не найден!')


def find_phone(phone):
    if os.path.exists('data.csv'):
        with open('data.csv', 'r', encoding='utf-8') as dt:
            reader = csv.reader(dt)
            sum_list = []
            for row in reader:
                if len(row) != 0:
                    sum_list.append(row[0].split(';'))
            count = 0
            for item in sum_list:
                if phone == item[2]:
                    wiew.answer(item)
                    count += 1
            if count == 0:
                wiew.answer(f'Человек с таким {phone} не найден!')
    else:
        wiew.answer('Файл не найден!')

def department(data):
    if os.path.exists('data.csv'):
        with open('data.csv', 'r', encoding='utf-8') as dt:
            reader = csv.reader(dt)
            sum_list = []
            for row in reader:
                if len(row) != 0:
                    sum_list.append(row[0].split(';'))
            count = 0
            for item in sum_list:
                if data == item[3]:
                    wiew.answer(item)
                    count += 1
            if count == 0:
                wiew.answer(f'Такой отдел {data} не найден!')
    else:
        wiew.answer('Файл не найден!')