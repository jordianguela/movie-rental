from abc import ABC, abstractmethod
from typing import List


class MovieType(ABC):
    @abstractmethod
    def calculate_rental_price(self, days_rented: int) -> float:
        pass

    @abstractmethod
    def calculate_frequent_renter_points(self, days_rented: int) -> int:
        pass


class RegularMovieType(MovieType):
    def calculate_rental_price(self, days_rented: int) -> float:
        rental_price = 2.0
        if days_rented > 2:
            rental_price += (days_rented - 2) * 1.5
        return rental_price

    def calculate_frequent_renter_points(self, days_rented: int) -> int:
        return 1


class NewReleaseMovieType(MovieType):
    def calculate_rental_price(self, days_rented: int) -> float:
        return days_rented * 3.0

    def calculate_frequent_renter_points(self, days_rented: int) -> int:
        return 2 if days_rented > 1 else 1


class ChildrenMovieType(MovieType):
    def calculate_rental_price(self, days_rented: int) -> float:
        rental_price = 1.5
        if days_rented > 3:
            rental_price += (days_rented - 3) * 1.5
        return rental_price

    def calculate_frequent_renter_points(self, days_rented: int) -> int:
        return 1


class Movie:
    def __init__(self, title: str, movie_type: MovieType):
        self.title = title
        self.movie_type = movie_type

    def calculate_rental_price(self, days_rented: int) -> float:
        return self.movie_type.calculate_rental_price(days_rented)

    def calculate_frequent_renter_points(self, days_rented):
        return self.movie_type.calculate_frequent_renter_points(days_rented)


class Rental:
    def __init__(self, movie: Movie, days_rented: int):
        self.days_rented = days_rented
        self.movie = movie

    def calculate_rental_price(self) -> float:
        return self.movie.calculate_rental_price(self.days_rented)

    def calculate_earned_rental_frequent_renter_points(self) -> int:
        return self.movie.calculate_frequent_renter_points(self.days_rented)

    def get_movie_title(self) -> str:
        return self.movie.title


class MovieStatementInfo:
    def __init__(self, movie_name: str, rental_price: float):
        self.movie_name = movie_name
        self.rental_price = rental_price


class Rentals:
    def __init__(self):
        self._rentals = []

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

    def generate_movie_statements_info(self) -> []:
        movie_statements_info = []
        for rental in self._rentals:
            movie_statements_info.append(MovieStatementInfo(rental.get_movie_title(), rental.calculate_rental_price()))
        return movie_statements_info


class Printer(ABC):
    @abstractmethod
    def generate_statement(self, customer_name: str, rentals: Rentals) -> str:
        pass


class DefaultStatementPrinter(Printer):
    def generate_statement(self, customer_name: str, rentals: Rentals) -> str:
        statement = "Rental Record for " + customer_name + "\n"

        for movie_statement_info in rentals.generate_movie_statements_info():
            statement += "\t" + movie_statement_info.movie_name + "\t" + str(movie_statement_info.rental_price) + "\n"

        statement += "Amount owed is " + str(rentals.calculate_total_owed_amount()) + "\n"
        statement += "You earned " + str(rentals.calculate_earned_frequent_renter_points()) + " frequent renter points"
        return statement


class HtmlStatementPrinter(Printer):
    def generate_statement(self, customer_name: str, rentals: Rentals) -> str:
        statement = "<h1>Rental Record for <em>" + customer_name + "</em></h1>\n"

        statement += "<table>\n"
        for movie_statement_info in rentals.generate_movie_statements_info():
            statement += "\t<tr><td>" + movie_statement_info.movie_name + "</td><td>" + str(
                movie_statement_info.rental_price) + "</td></tr>\n"
        statement += "</table>\n"

        statement += "<p>Amount owed is <em>" + str(rentals.calculate_total_owed_amount()) + "</em></p>\n"
        statement += "<p>You earned <em>" + str(
            rentals.calculate_earned_frequent_renter_points()) + "</em> frequent renter points</p>"
        return statement


class Customer:
    def __init__(self, name: str):
        self.name = name
        self.rentals = Rentals()

    def print_statement(self, printer: Printer):
        return printer.generate_statement(self.name, self.rentals)

    def add_rental(self, rental: Rental):
        self.rentals.add(rental)