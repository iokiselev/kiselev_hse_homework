class Employee:
    def __init__(self, name, experience):
        self.name = name
        self.experience = experience

        self.grade = 1

    def grade_up(self):
        self.grade += 1

    def publish_grade(self):
        print(self.name, self.grade)

    def check_if_it_is_time_for_upgrade(self):
        pass

class Designer(Employee):
    def __init__(self, name, experience):
        super().__init__(name, experience)

    def check_if_it_is_time_for_upgrade(self):
        self.experience += 1
        international_award = 2

        if (self.experience + 2 * international_award) % 7 == 0:
            self.grade_up()

        return self.publish_grade()
