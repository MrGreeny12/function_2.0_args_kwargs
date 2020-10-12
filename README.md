1. Создать приложение "Телефонная книга".
класс Contact имеет следующие поля:
- Имя, фамилия, телефонный номер - обязательные поля;
- Избранный контакт - необязательное поле. По умолчанию False;
- Дополнительная информация(email, список дополнительных номеров, ссылки на соцсети) - необходимо использовать *args, \**kwargs.

Переопределить "магический" метод __str__ для красивого вывода контакта.
Вывод контакта должен быть следующим
```
    jhon = Contact('Jhon', 'Smith', '+71234567809', telegram='@jhony', email='jhony@smith.com')
    print(jhon)
```
Вывод 
```
Имя: Jhon
Фамилия: Smith
Телефон: +71234567809
В избранных: нет
Дополнительная информация:
	 telegram : @jhony
	 email : jhony@smith.com
```

2. класс PhoneBook:
- Название телефонной книги - обязательное поле;
- Телефонная книга должна работать с классами Contact.

Методы:
- Вывод контактов из телефонной книги;
- Добавление нового контакта;
- Удаление контакта по номеру телефона;
- Поиск всех избранных номеров;
- Поиск контакта по имени и фамилии.

\*3. Продвинутый print (необязательное задание)
Разработать свою реализацию функции print - adv_print. Она ничем не должна отличаться от классической функции кроме трех новых необязательных аргументов:
- start - с чего начинается вывод. По умолчанию пустая строка;
- max_line - максимальная длин строки при выводе. Если строка превышает max_line, то вывод автоматически переносится на новую строку;
- in_file - аргумент, определяющий будет ли записан вывод ещё и в файл.
Сигнатура функции должна быть такой
```
def adv_print(*args, **kwargs)
```
