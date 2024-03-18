class Vacancy:
    def __init__(self, title, link, salary, description):
        self.title = title
        self.link = link
        self.salary = self.validate_salary(salary)
        self.description = description

    def validate_salary(self, salary):
        """Валидирует и возвращает зарплату."""
        return salary or "Зарплата не указана"
