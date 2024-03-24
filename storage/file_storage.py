from abc import ABC, abstractmethod
from typing import Any, List


class FileStorage(ABC):
    @abstractmethod
    def save_data(self, data: List[Any], filepath: str) -> None:
        """Сохраняет данные в файл."""
        pass

    @abstractmethod
    def load_data(self, filepath: str) -> List[Any]:
        """Загружает данные из файла."""
        pass
