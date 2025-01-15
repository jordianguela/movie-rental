from enum import Enum


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

    def calculate_rental_price(self) -> int:
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


class Customer:
    def __init__(self, name: str):
        self.name = name
        self._rentals = []

    def statement(self):
        total_amount = 0
        frequent_renter_points = 0
        result = "Rental Record for " + self.name + "\n"

        for rental in self._rentals:
            this_amount = rental.calculate_rental_price()

            # add frequent renter points
            frequent_renter_points += 1
            # add bonus for a two day new release rental
            if (rental.movie.price_code == MoviePriceCode.NEW_RELEASE) and rental.days_rented > 1:
                frequent_renter_points += 1

            # show figures for this rental
            result += "\t" + rental.movie.title + "\t" + str(this_amount) + "\n"
            total_amount += this_amount

        # add footer lines
        result += "Amount owed is " + str(total_amount) + "\n"
        result += "You earned " + str(frequent_renter_points) + " frequent renter points"

        return result

    def add_rental(self, rental: Rental):
        self._rentals.append(rental)
