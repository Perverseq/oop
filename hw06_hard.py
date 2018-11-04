import os
# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"
# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла


class Arbeiter(object):

    def __init__(self, name, surname, salary, post, hours):
        self.name = name
        self.surname = surname
        self.salary = int(salary)
        self.post = post
        self.norm_hours = int(hours)
        self.real_hours = int(0)
        self.payment = int(0)

    def __str__(self):
        return f"Работник: {self.name:7} {self.surname:8} Полный оклад: {self.salary:5} " \
               f"Должность: {self.post:12} Норма часов: {self.norm_hours:3} Отработано часов:" \
               f" {self.real_hours:3} Зарплата за месяц: {self.payment:5}"

    def add_hour_for_worker(self, hours):
        self.real_hours = hours

    def set_payment(self):
        pay_per_hour = int(self.salary / self.norm_hours)
        if int(self.norm_hours) > int(self.real_hours):
            self.payment = pay_per_hour * int(self.real_hours)
        elif self.norm_hours == self.real_hours:
            self.payment = self.salary
        else:
            self.payment = self.salary + 2 * (int(self.real_hours) - int(self.norm_hours)) * pay_per_hour


def get_hours(workers):
    with open(os.path.abspath('data/hours_of'), 'r', encoding='utf-8') as hours_of:
        for line in hours_of:
            string_line = line.split()
            for worker in workers:
                if worker.name == string_line[0] and worker.surname == string_line[1]:
                    worker.add_hour_for_worker(string_line[2])


def get_workers():
    workers = []
    count = 0
    with open(os.path.abspath('data/workers'), 'r', encoding='utf-8') as workers_list:
        for line in workers_list:
            if count > 0:
                string_line = line.split()
                workers.append(Arbeiter(string_line[0], string_line[1], string_line[2], string_line[3], string_line[4]))
            count += 1
    get_hours(workers)
    return workers


def main():
    workers = get_workers()
    for worker in workers:
        worker.set_payment()
        print(worker)


if __name__ == '__main__':
    main()
