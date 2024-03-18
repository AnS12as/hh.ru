import json


class JSONStorage:
    def __init__(self, filepath='vacancies.json'):
        self.filepath = filepath

    def save_vacancies(self, vacancies):
        with open(self.filepath, 'w', encoding='utf-8') as file:
            json.dump(vacancies, file, ensure_ascii=False, indent=4)

def save_vacancies(self, vacancies):
    print(f"Сохранение данных в {self.filepath}...")
    with open(self.filepath, 'w', encoding='utf-8') as file:
        json.dump(vacancies, file, ensure_ascii=False, indent=4)
    print("Данные успешно сохранены.")
