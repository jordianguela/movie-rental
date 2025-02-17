from domain.Printer import Printer
from domain.Rentals import Rentals


class HtmlStatementPrinter(Printer):
    def generate_statement(self, customer_name: str, rentals: Rentals) -> str:
        statement = "<h1>Rental Record for <em>" + customer_name + "</em></h1>\n"

        statement += "<table>\n"
        for rental in rentals:
            statement += "\t<tr><td>" + rental.get_movie_title() + "</td><td>" + str(
                rental.calculate_rental_price()) + "</td></tr>\n"
        statement += "</table>\n"

        statement += "<p>Amount owed is <em>" + str(rentals.calculate_total_owed_amount()) + "</em></p>\n"
        statement += "<p>You earned <em>" + str(
            rentals.calculate_earned_frequent_renter_points()) + "</em> frequent renter points</p>"
        return statement