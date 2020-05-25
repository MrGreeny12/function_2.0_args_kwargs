class Contact:
    '''
    информация о контакте
    '''
    def __init__(self, name, surname, number, favorite=False, **kwargs):
        self.name = name
        self.surname = surname
        self.number = number
        if favorite == False:
            self.favorite = 'нет'
        else:
            self.favorite = 'да'
        self.other_information = kwargs
        # дополнительную информацию о контакте хранить в словаре. остальное в init

    def print_oth_inf(self):
        strings = []
        for key, value in self.other_information.items():
            strings.append("{}: {}".format(key.capitalize(), value))
        result = "\n".join(strings)
        return result

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \nТелефон: {self.number} \nВ избранных: {self.favorite} \nДополнительная информация: \n{self.print_oth_inf()}'

class PhoneBook:
    '''
    информация в телефонной книге в виде словаря экземпляров класса и их id
    '''
    def __init__(self):
        self.name_book = self
        self.bd = {}
        self.id = 1

    def add_contact(self, contact):
        self.bd[self.id] = contact
        self.id += 1
        print(f'Контакт {contact.name} {contact.surname} добавлен!')

    def print_contact(self, contact):
        for item in self.bd.values():
            if contact == item:
                print(contact)
            else:
                continue

    def delete_contact(self, number):
        for key, value in self.bd.items():
            if value.number == number:
                del self.bd[key]
                print(f'Контакт с номером телефона {number} удален.')
                break

    def favorite_search(self):
        count = 1
        print('Список избранных контактов: ')
        for key, value in self.bd.items():
            count += 1
            if value.favorite == 'да':
                print(value.name, value.surname)
            elif (value.favorite == 'нет') and (count < len(self.bd)):
                continue
            elif (value.favorite == 'нет') and (count == len(self.bd)):
                print('Нет избранных контактов')

    def surname_search(self, surname):
        print('Результат поиска по фамилии: ')
        count = 1
        contacts = 0
        for key, value in self.bd.items():
            count += 1
            if value.surname == surname:
                print(value)
                contacts += 1
            elif (value.surname != surname) and (count < len(self.bd)):
                continue
            elif (value.surname != surname) and (count == len(self.bd)) and (contacts == 0):
                print('Таких контактов нет')

if __name__ == '__main__':
    jhon = Contact('Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com')
    mikey = Contact('Mikey', 'Jonson', '+71934567809', favorite=True, telegram='@jhony', email='jhony@smith.com')
    print(jhon)
    test_book = PhoneBook()
    test_book.add_contact(jhon)
    test_book.add_contact(mikey)
    test_book.print_contact(jhon)
    test_book.favorite_search()
    test_book.surname_search('Smith')
    test_book.delete_contact('+71934567809')
    print(test_book.bd)

