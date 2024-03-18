import requests
from abc import ABC, abstractmethod


class APIConnector(ABC):
    @abstractmethod
    def get_vacancies(self, query, area):
        """Извлекает вакансии по заданному запросу для определенной области."""
        pass


class HeadHunterAPI(APIConnector):
    BASE_URL = "https://api.hh.ru/vacancies"

    def get_vacancies(self, query, area="113"):
        """Получает вакансии по запросу для заданной области (Россия)."""
        params = {"text": query, "area": area}
        response = requests.get(self.BASE_URL, params=params)
        response.raise_for_status()
        return response.json()
