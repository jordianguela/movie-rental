from abc import ABC, abstractmethod


class MovieType(ABC):
    @abstractmethod
    def calculate_rental_price(self, days_rented: int) -> float:
        pass

    @abstractmethod
    def calculate_frequent_renter_points(self, days_rented: int) -> int:
        pass
