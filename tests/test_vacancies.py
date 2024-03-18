import os
import unittest
import json
from models.vacancy import Vacancy
from storage.json_storage import JSONStorage


class TestVacancyModel(unittest.TestCase):
    def test_vacancy_creation(self):
        """Тестирование создания объекта вакансии."""
        vacancy = Vacancy("Python Developer", "https://api.hh.ru/vacancies", 100000, "Develop cool software")
        self.assertEqual(vacancy.title, "Python Developer")
        self.assertEqual(vacancy.link, "https://api.hh.ru/vacancies")
        self.assertEqual(vacancy.salary, 100000)
        self.assertEqual(vacancy.description, "Develop cool software")


class TestJSONStorage(unittest.TestCase):
    def test_vacancy_saving(self):
        """Тестирование сохранения вакансии в JSON файл."""
        vacancies = [Vacancy("Python Developer", "https://api.hh.ru/vacancies", 100000, "Develop cool software")]
        storage = JSONStorage("test_vacancies.json")
        storage.save_vacancies([vars(v) for v in vacancies])

        # Проверка, что файл был создан
        self.assertTrue(os.path.exists("test_vacancies.json"))

        # Проверка содержимого файла
        with open("test_vacancies.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            self.assertEqual(len(data), 1)
            self.assertEqual(data[0]['title'], "Python Developer")
            self.assertEqual(data[0]['link'], "https://api.hh.ru/vacancies")
            self.assertEqual(data[0]['salary'], 100000)
            self.assertEqual(data[0]['description'], "Develop cool software")

        os.remove("test_vacancies.json")


if __name__ == '__main__':
    unittest.main()
