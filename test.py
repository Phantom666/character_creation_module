import datetime as dt

# Объявите класс Quest с методами и свойствами.
class Quest:
    """Создание квеста"""

    def __init__(self, name, description, goal):
        self.name = name
        self.description = description
        self.goal = goal
        self.start_time = None
        self.end_time = None

    def accept_quest(self):
        if self.end_time:
            return 'С этим квестом вы уже справились.'
        self.start_time = (dt.datetime.time(dt.datetime.now())
                           .strftime('%H:%M:S'))
        return f'Начало "{self.name}" положено.'

    def pass_quest(self):
        if self.start_time is None:
            return 'Нельзя завершить то, что не имеет начала!'
        self.end_time = (dt.datetime.time(dt.datetime.now())
                         .strftime('%H:%M:S'))
        comletion_time = self.end_time - self.start_time
        return (f'Квест "{self.name}" окончен. '
                f'Время выполнения квеста: {comletion_time}')

    def __str__(self):
        res = f'Цель квеста {self.name} - {self.goal}.'
        if self.end_time:
            return res + f' Квест завершён.'
        if self.start_time:
            return res + f' Квест выполняется.'
        return res



# В этих переменных содержатся значения, которые нужно передать
# в качестве аргументов в экземпляр класса Quest.

quest_name = 'Сбор пиксельники'
quest_goal = 'Соберите 12 ягод пиксельники.'
quest_description = '''
В древнем лесу Кодоборье растёт ягода "пиксельника".
Она нужна для приготовления целебных снадобий.
Соберите 12 ягод пиксельники.'''

# Создайте экземпляр класса Quest.
new_quest = Quest(quest_name, quest_description, quest_goal)
print(dt.datetime.time(dt.datetime.now()).strftime('%H:%M:%S'))