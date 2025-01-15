from abc import ABC, abstractmethod
from enum import Enum
from typing import List


class MovieType(ABC):
    @abstractmethod
    def calculate_rental_price(self, days_rented: int) -> float:
        pass

    @abstractmethod
    def calculate_earned_rental_frequent_renter_points(self, days_rented: int) -> int:
        pass


class RegularMovie(MovieType):
    def calculate_rental_price(self, days_rented: int) -> float:
        rental_price = 2.0
        if days_rented > 2:
            rental_price += (days_rented - 2) * 1.5
        return rental_price

    def calculate_earned_rental_frequent_renter_points(self, days_rented: int) -> int:
        return 1


class NewReleaseMovie(MovieType):
    def calculate_rental_price(self, days_rented: int) -> float:
        return days_rented * 3.0

    def calculate_earned_rental_frequent_renter_points(self, days_rented: int) -> int:
        return 2 if days_rented > 1 else 1


class ChildrenMovie(MovieType):
    def calculate_rental_price(self, days_rented: int) -> float:
        rental_price = 1.5
        if days_rented > 3:
            rental_price += (days_rented - 3) * 1.5
        return rental_price

    def calculate_earned_rental_frequent_renter_points(self, days_rented: int) -> int:
        return 1


class Movie:
    def __init__(self, title: str, movie_type: MovieType):
        self.title = title
        self.movie_type = movie_type


class Rental:
    def __init__(self, movie: Movie, days_rented: int):
        self.days_rented = days_rented
        self.movie = movie

    def calculate_rental_price(self) -> float:
        return self.movie.movie_type.calculate_rental_price(self.days_rented)


class MovieStatementInfo:
    def __init__(self, movie_name: str, rental_price: float):
        self.movie_name = movie_name
        self.rental_price = rental_price


class Printer(ABC):
    @abstractmethod
    def generate_statement(self,
                           customer_name: str,
                           movie_statement_info: [],
                           total_owed_amount: float,
                           frequent_renter_points: int) -> str:
        pass


class DefaultStatementPrinter(Printer):
    def generate_statement(self,
                           customer_name: str,
                           movie_statements_info: List[MovieStatementInfo],
                           total_owed_amount: float,
                           frequent_renter_points: int) -> str:
        statement = "Rental Record for " + customer_name + "\n"

        for movie_statement_info in movie_statements_info:
            statement += "\t" + movie_statement_info.movie_name + "\t" + str(movie_statement_info.rental_price) + "\n"

        statement += "Amount owed is " + str(total_owed_amount) + "\n"
        statement += "You earned " + str(frequent_renter_points) + " frequent renter points"
        return statement


class HtmlStatementPrinter(Printer):
    def generate_statement(self,
                           customer_name: str,
                           movie_statements_info: List[MovieStatementInfo],
                           total_owed_amount: float,
                           frequent_renter_points: int) -> str:
        statement = "<h1>Rental Record for <em>" + customer_name + "</em></h1>\n"

        statement += "<table>\n"
        for movie_statement_info in movie_statements_info:
            statement += "\t<tr><td>" + movie_statement_info.movie_name + "</td><td>" + str(movie_statement_info.rental_price) + "</td></tr>\n"
        statement += "</table>\n"

        statement += "<p>Amount owed is <em>" + str(total_owed_amount) + "</em></p>\n"
        statement += "<p>You earned <em>" + str(frequent_renter_points) + "</em> frequent renter points</p>"
        return statement


class Customer:
    def __init__(self, name: str):
        self.name = name
        self._rentals = []

    def print_statement(self, printer: Printer):
        total_owed_amount = 0
        frequent_renter_points = 0
        movie_statements_info = []

        for rental in self._rentals:
            rental_price = rental.calculate_rental_price()
            movie_statements_info.append(MovieStatementInfo(rental.movie.title, rental_price))
            frequent_renter_points += rental.movie.movie_type.calculate_earned_rental_frequent_renter_points(rental.days_rented)
            total_owed_amount += rental_price

        return printer.generate_statement(self.name, movie_statements_info, total_owed_amount, frequent_renter_points)

    def add_rental(self, rental: Rental):
        self._rentals.append(rental)
