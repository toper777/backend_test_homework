class Contact:
    def __init__(self,
                 name: str,
                 year_birth: int,
                 is_programmer) -> None:
        self.name = name
        self.year_birth = year_birth
        self.is_programmer = is_programmer

    def age_define(self) -> str:
        if 1946 < self.year_birth < 1980:
            return 'Олдскул'
        if self.year_birth >= 1980:
            return 'Молодой'
        return 'Старейшина'

    def programmer_define(self) -> str:
        if self.is_programmer:
            return 'Программист'
        return 'Нормальный'

    def show_contact(self) -> str:
        return (f'{self.name}, '
                f'категория: {self.age_define()}, '
                f'статус: {self.programmer_define()}')

    def print_contact(self) -> None:
        print(self.show_contact())


me = Contact('Tikhon', 1974, False)
me.print_contact()
