class Employee:
    def __init__(self, name, seniority, awards):
        self.name = name
        self.seniority = seniority
        self.awards = awards

        self.grade = 1

    def grade_up(self):
        """Повышает уровень сотрудника"""
        self.grade += 1

    def publish_grade(self):
        """Публикация результатов аккредитации сотрудников"""
        print(self.name, self.grade)


class Developer(Employee):
    def __init__(self, name, seniority, awards=0):
        super().__init__(name, seniority, awards=0)

    def check_if_it_is_time_for_upgrade(self):
        # для каждой аккредитации увеличиваем счетчик на 1
        # пока считаем, что все разработчики проходят аккредитацию
        self.seniority += 1

        # условие повышения сотрудника из презентации
        if self.seniority % 5 == 0:
            self.grade_up()

        # публикация результатов
        return self.publish_grade()


class Designer(Employee):
    def __init__(self, name, seniority, awards):
        super().__init__(name, seniority, awards)

    def check_if_it_is_time_for_upgrade(self):
        if self.seniority == 0:
            self.seniority = 1 + self.awards * 2
        else:
            self.seniority += 1
        if self.seniority % 7 == 0:
            self.grade_up()

        return self.publish_grade()
