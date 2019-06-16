OPTIONAL_FIELDS = ['phone2', 'vk', 'facebook', 'linkedn', 'telegram', 'viber', 'whatsapp']


class Contact:

    def __init__(self, first_name, last_name, phone, favorite=False, *args, **kwargs):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.favorite = favorite
        if args:
            self.phone2 = args[0]
            self.vk = args[1]
            self.facebook = args[2]
            self.linkend = args[3]
            self.telegram = args[4]
            self.viber = args[5]
            self.whatsapp = args[6]
        elif kwargs:
            for var_name, var_value in kwargs.items():
                if var_name in OPTIONAL_FIELDS:
                    setattr(self, var_name, var_value)
                else:
                    raise ValueError(var_name)

    @property
    def is_favorite(self):
        if self.favorite:
            return 'да'
        return 'нет'

    def __str__(self):
        opt_fields = [''.join([field, ':', getattr(self, field)]) for field in OPTIONAL_FIELDS if hasattr(self, field)]
        return '\n'.join([
            'Имя: ' + self.first_name, 'Фамилия: ' + self.last_name, 'Т,елефон: ' + self.phone,
            'В избранных: ' + self.is_favorite, 'Дополнительная информация:',
            '\n'.join(opt_fields)
        ])


class PhoneBook:

    def __init__(self, phonebook_name, *args):
        self.name = phonebook_name
        self.contact_list = []
        if args:
            for item in args:
                if type(item) == Contact:
                    self.contact_list.append(item)
                else:
                    raise ValueError(item, type(item))

    def show_all_contact(self):
        for contact in self.contact_list:
            print('----------------------------------')
            print(contact)

    def add_contact(self, first_name, last_name, phone, favorite=False, *args, **kwargs):
        self.contact_list.append(Contact(first_name, last_name, phone, favorite, *args, **kwargs))

    def del_contact(self, phone):
        for contact in self.contact_list:
            if contact.phone == phone:
                self.contact_list.remove(contact)
                return True
        return False

    def find_favorites(self):
        return [favorite for favorite in self.contact_list if favorite.favorite]

    def find_by_fio(self, first_name, last_name):
        return [contact for contact in self.contact_list
            if contact.first_name == first_name and contact.last_name == last_name]


def adv_print(*args, **kwargs):
    p_args = (None, None, None, None)
    if args:
        def arg(i):
            if i < len(args):
                return args[i]
            return None
        p_args = (arg(i) for i in range(4))
    text, start, max_line, in_file = p_args
    if kwargs:
        text = kwargs.get('text')
        start = kwargs.get('start')
        max_line = kwargs.get('max_line')
        in_file = kwargs.get('in_file')
    if text:
        lines = []
        if max_line:
            chunk, chunk_size = len(text), max_line
            lines = [text[i:i+chunk_size] + '\n' for i in range(0, chunk, chunk_size) ]
        else:
            lines.append(text)
        if in_file:
            with open(in_file, 'w', encoding='utf-8') as f:
                print(*lines, file=f)
        print(*lines)
    print('')


if __name__=='__main__':
    lt = Contact(
        first_name='Lev', last_name='Tolstoy', phone='+7900000000', favorite=False,
        facebook='http://facebook.com/lev_tolstoy', vk='http://vk.com/lev_tolstoy',
        telegram='@lev_tolstoy'
    )

    vm = Contact(
        first_name='Vladimir', last_name='Mayakovsky', phone='+7900000001', favorite=True,
        facebook='http://facebook.com/mayakovsky', vk='http://vk.com/mayakovsky',
        telegram='@mayakovsky'
    )

    ap = Contact(
        first_name='Aleksandr', last_name='Pushkin', phone='+7900000002', favorite=True,
        facebook='http://facebook.com/pushkin', vk='http://vk.com/pushkin',
        telegram='@pushkin'
    )

    book = PhoneBook('classics', lt, vm, ap)

    book.show_all_contact()

    book.add_contact(first_name='Vladimir', last_name='Nabokov', phone='+790004345', favorite=True)

    favorites = book.find_favorites()
    print('===============================================')
    print('FAVORITES')
    for favorite in favorites:
        print('--------------------------------')
        print(favorite)

    print('================================================')
    contacts = book.find_by_fio('Vladimir', 'Nabokov')
    if len(contacts) > 0:
        finded_contact = contacts[0]
        print('Finded ', len(contacts), ' contacts')
        print('Contact ', finded_contact, ' is now deleted')
        book.del_contact(finded_contact.phone)

    print('=============TEST1 ADV PRINT============')
    adv_print(
        text='Lorem ipsum dolor sit amet, consectetur adipiscing elit.',
        start='==>', max_line=7, in_file='log.txt'
    )
    print('=============TEST2 ADV PRINT============')
    adv_print('Lorem ipsum dolor sit amet, consectetur adipiscing elit.',)
