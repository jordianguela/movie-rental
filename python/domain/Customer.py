from domain.Printer import Printer
from domain.Rental import Rental
from domain.Rentals import Rentals


class Customer:
    def __init__(self, name: str):
        self.name = name
        self.rentals = Rentals()

    def print_statement(self, printer: Printer):
        return printer.generate_statement(self.name, self.rentals)

    def add_rental(self, rental: Rental):
        self.rentals.add(rental)
