import json
from typing import Any, List
from .file_storage import FileStorage


class JSONStorage(FileStorage):
    def __init__(self, filepath="vacancies.json"):
        self.filepath = filepath

    def save_data(self, data: List[Any], filepath: str = None) -> None:
        if filepath is not None:
            self.filepath = filepath
        with open(self.filepath, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
            print("Вакансии сохранены")

    def load_data(self, filepath: str = None) -> List[Any]:
        if filepath is not None:
            self.filepath = filepath
        try:
            with open(self.filepath, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"File {self.filepath} not found.")
            return []
