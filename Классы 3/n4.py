# 4)ContactList
# Создайте класс ContactList, который должен наследоваться от
# встроенного класса list. В нем должен быть реализован метод
# search_by_name, который должен принимать имя, и возвращать список
# всех совпадений. Замените all_contacts = [ ] на all_contacts =
# ContactList(). Создайте несколько контактов, используйте метод
# search_by_name.
contacts = ['Nursultan','Bektur','Baktybek','Janarabek','Bekzhan']

class ContactList(list):
    def search_by_name(name):
        pass