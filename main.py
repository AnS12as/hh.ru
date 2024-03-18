from api.headhunter import HeadHunterAPI
from models.vacancy import Vacancy
from storage.json_storage import JSONStorage


def user_interaction():
    api = HeadHunterAPI()
    storage = JSONStorage()

    while True:
        print("\n1. Запросить вакансии с hh.ru")
        print("2. Сохранить последние полученные вакансии в файл")
        print("3. Выход")
        choice = input("Выберите действие: ")

        if choice == '1':
            query = input("Введите запрос для поиска вакансий: ")
            vacancies_data = api.get_vacancies(query)
            vacancies = [
                Vacancy(item['name'], item['alternate_url'],
                        item.get('salary', {}).get('from') if item.get('salary') else "Зарплата не указана",
                        item['snippet']['requirement'])
                for item in vacancies_data['items']
            ]
            print("\nНайденные вакансии:")
            for i, vacancy in enumerate(vacancies, start=1):
                print(f"{i}. {vacancy.title} - {vacancy.link} - {vacancy.salary}")
            last_vacancies = vacancies  # Сохраняем вакансии для возможности последующего сохранения

        elif choice == '2':
            if 'last_vacancies' in locals():
                storage.save_vacancies([vars(v) for v in last_vacancies])
                print("Вакансии сохранены в файл.")
            else:
                print("Сначала выполните поиск вакансий.")

        elif choice == '3':
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите один из предложенных вариантов.")


if __name__ == "__main__":
    user_interaction()
