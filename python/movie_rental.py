from abc import ABC, abstractmethod
from enum import Enum
from typing import List


class MoviePriceCode(Enum):
    REGULAR = 0
    NEW_RELEASE = 1
    CHILDREN = 2


class Movie:
    def __init__(self, title: str, price_code: MoviePriceCode):
        self.title = title
        self.price_code = price_code


class Rental:
    def __init__(self, movie: Movie, days_rented: int):
        self.days_rented = days_rented
        self.movie = movie

    def calculate_rental_price(self) -> float:
        this_amount = 0.0

        if self.movie.price_code == MoviePriceCode.REGULAR:
            this_amount += 2
            if self.days_rented > 2:
                this_amount += (self.days_rented - 2) * 1.5
        elif self.movie.price_code == MoviePriceCode.NEW_RELEASE:
            this_amount += self.days_rented * 3
        elif self.movie.price_code == MoviePriceCode.CHILDREN:
            this_amount += 1.5
            if self.days_rented > 3:
                this_amount += (self.days_rented - 3) * 1.5

        return this_amount


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


class Customer:
    def __init__(self, name: str):
        self.name = name
        self._rentals = []

    def statement(self):
        total_owed_amount = 0
        frequent_renter_points = 0
        movie_statements_info = []

        for rental in self._rentals:
            rental_price = rental.calculate_rental_price()
            movie_statements_info.append(MovieStatementInfo(rental.movie.title, rental_price))
            frequent_renter_points += 1
            if (rental.movie.price_code == MoviePriceCode.NEW_RELEASE) and rental.days_rented > 1:
                frequent_renter_points += 1
            total_owed_amount += rental_price

        default_statement_printer = DefaultStatementPrinter()
        return default_statement_printer.generate_statement(self.name, movie_statements_info, total_owed_amount, frequent_renter_points)

    def add_rental(self, rental: Rental):
        self._rentals.append(rental)
