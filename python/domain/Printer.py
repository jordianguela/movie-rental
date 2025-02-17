from abc import ABC, abstractmethod

from domain.Rentals import Rentals


class Printer(ABC):
    @abstractmethod
    def generate_statement(self, customer_name: str, rentals: Rentals) -> str:
        pass
