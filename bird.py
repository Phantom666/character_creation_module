

class Bird:
    def __init__(self, name:str, size:str):
        self.name = name
        self.size = size

    def describe(self, full: bool = False) -> str:
        desc = f'Размер птицы {self.name} - {self.size}'
        return desc


class Parrot(Bird):
    def __init__(self, name:str, size:str, color:str):
        super().__init__(name, size)
        self.color = color

    def describe(self, full: bool = False) -> str:
        if not full:
            return super().describe()
        full_describe = (f'Попугай {self.name} - заметная птица, окрас её '
                         f'перьев - {self.color}. Интересный факт: попугаи '
                         f'чувствуют ритм, а вовсе не бездумно двигаются '
                         f'под музыку. Если сменить композицию, то темп и '
                         f'движения птицы изменится.')
        return full_describe

    def repeat(self, phrase) -> str:
        res = f'Попугай {self.name} говорит: {phrase}'
        return res



class Penguin(Bird):
    def __init__(self, name:str, size:str, genus:str):
        super().__init__(name, size)
        self.genus = genus

    def describe(self, full: bool = False) -> str:
        if not full:
            return super().describe()
        full_describe = (f'Размер пингвина {self.name} из рода '
                         f'{self.genus} — {self.size}. Интересный факт: '
                         f'однажды группа геологов-разведчиков похитила '
                         f'пингвинье яйцо, и их принялась преследовать вся '
                         f'стая, не пытаясь, впрочем, при этом нападать. '
                         f'Посовещавшись, похитители вернули птицам яйцо, и те '
                         f'отстали.')
        return full_describe

    def swimming(self) -> str:
        return f'Пингвин {self.name} плавает со средней скоростью 11 км/ч'
