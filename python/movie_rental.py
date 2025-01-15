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


class Customer:
    def __init__(self, name: str):
        self.name = name
        self._rentals = []

    def statement(self):
        total_amount = 0
        frequent_renter_points = 0
        result = "Rental Record for " + self.name + "\n"

        for each in self._rentals:
            this_amount = 0.0

            # determine amounts for each line
            if each.movie.price_code == MoviePriceCode.REGULAR:
                this_amount += 2
                if each.days_rented > 2:
                    this_amount += (each.days_rented - 2) * 1.5
            elif each.movie.price_code == MoviePriceCode.NEW_RELEASE:
                this_amount += each.days_rented * 3
            elif each.movie.price_code == MoviePriceCode.CHILDREN:
                this_amount += 1.5
                if each.days_rented > 3:
                    this_amount += (each.days_rented - 3) * 1.5

            # add frequent renter points
            frequent_renter_points += 1
            # add bonus for a two day new release rental
            if (each.movie.price_code == MoviePriceCode.NEW_RELEASE) and each.days_rented > 1:
                frequent_renter_points += 1

            # show figures for this rental
            result += "\t" + each.movie.title + "\t" + str(this_amount) + "\n"
            total_amount += this_amount

        # add footer lines
        result += "Amount owed is " + str(total_amount) + "\n"
        result += "You earned " + str(frequent_renter_points) + " frequent renter points"

        return result

    def add_rental(self, rental: Rental):
        self._rentals.append(rental)
