from domain.Rental import Rental


class Rentals:
    def __init__(self):
        self._rentals = []

    def __iter__(self):
        return iter(self._rentals)

    def add(self, rental: Rental):
        self._rentals.append(rental)

    def calculate_total_owed_amount(self) -> float:
        total_owed_amount = 0.0
        for rental in self._rentals:
            rental_price = rental.calculate_rental_price()
            total_owed_amount += rental_price
        return total_owed_amount

    def calculate_earned_frequent_renter_points(self):
        frequent_renter_points = 0
        for rental in self._rentals:
            frequent_renter_points += rental.calculate_earned_rental_frequent_renter_points()
        return frequent_renter_points
