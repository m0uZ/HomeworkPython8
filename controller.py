import wiew
import log
import operation


def button_click():
    wiew.hello()
    choise = wiew.button()
    log.log(choise)
    while choise != 'q':
        if choise == '1':
            operation.export_data()
        elif choise == '2':
            what_find = input('Для поиска по фамилии введите "1"\nДля поиска по имени введите "2"\nДля поиска по номеру телефона введите "3"\nДля поиска по отделу введите "4"\n')
            if what_find == '1': operation.find_surname(input('Введите фамилию: '))
            if what_find == '2': operation.find_name(input('Введите имя: '))
            if what_find == '3': operation.find_phone(input('Введите телефон: '))
            if what_find == '4': operation.department(input('Введите отдел: '))


        choise = wiew.button()