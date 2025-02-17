from domain.Printer import Printer
from domain.Rentals import Rentals


class DefaultStatementPrinter(Printer):
    def generate_statement(self, customer_name: str, rentals: Rentals) -> str:
        statement = "Rental Record for " + customer_name + "\n"

        for rental in rentals:
            statement += "\t" + rental.get_movie_title() + "\t" + str(rental.calculate_rental_price()) + "\n"

        statement += "Amount owed is " + str(rentals.calculate_total_owed_amount()) + "\n"
        statement += "You earned " + str(rentals.calculate_earned_frequent_renter_points()) + " frequent renter points"
        return statement
