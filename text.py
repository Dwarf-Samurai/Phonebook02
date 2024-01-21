main_menu = ['Главное меню',
             'Открыть файл',
             'Сохранить',
             'Показать контакты',
             'Создать контакт',
             'Найти контакт',
             'Изменить контакт',
             'Удалить контакт',
             'Выход']

main_menu_choice = 'Выберите пукт меню: '
load_successful = 'Телефонная книга загружена!'
save_successful = 'Телефонная книга успешно СОХРАНЕНА!'

empty_phone_book = 'Пусто или не открыт файл!'

new_contact = ['Введите имя: ',
               'Введите номер телефона: ',
               'Введите примечание: ',]

def new_contact_added_successful(name: str) -> str:
    return f'Контакт {name} успешно добавлен!'

input_search_word = 'Введите слово для поиска: '

def contacts_not_found(word: str) -> str:
    return f'Контакты содержащие {word} не найдены!'

input_id_change_contact = 'Введите ID контакта, который хотите изменить: '

change_contact = ['Введите новое имя или ENTER, чтобы перейти к редактированию номера: ',
                'Введите новый номер или ENTER, чтобы перейти к редактированию примечания: ',
                'Введите новое примечание или ENTER, чтобы оставить без изменений: ']

def contact_changed_successful(name: str) -> str:
    return f'Контакт {name} успешно изменен!'

input_id_delete_contact = 'Введите ID контакта, который хотите УДАЛИТЬ: '

def contact_deleted_successful(name: str) -> str:
    return f'Контакт {name} успешно УДАЛЕН!'