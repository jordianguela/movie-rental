from enum import Enum


class MoviePriceCode(Enum):
    REGULAR = 0
    NEW_RELEASE = 1
    CHILDREN = 2


class Movie:
    def __init__(self, title: str, price_code: MoviePriceCode):
        self.title = title
        self.price_code = price_code

    def get_price_code(self) -> MoviePriceCode:
        return self.price_code

    def set_price_code(self, price_code: MoviePriceCode):
        self.price_code = price_code

    def get_title(self) -> str:
        return self.title


class Rental:
    def __init__(self, movie: Movie, days_rented: int):
        self.daysRented = days_rented
        self.movie = movie

    def get_days_rented(self) -> int:
        return self.daysRented

    def get_movie(self) -> Movie:
        return self.movie


class Customer:
    def __init__(self, name: str):
        self._rentals = []
        self.name = name

    def get_name(self):
        return self.name

    def statement(self):
        total_amount = 0
        frequent_renter_points = 0
        result = "Rental Record for " + self.get_name() + "\n"

        for each in self._rentals:
            this_amount = 0.0

            # determine amounts for each line
            if each.get_movie().get_price_code() == MoviePriceCode.REGULAR:
                this_amount += 2
                if each.get_days_rented() > 2:
                    this_amount += (each.get_days_rented() - 2) * 1.5
            elif each.get_movie().get_price_code() == MoviePriceCode.NEW_RELEASE:
                this_amount += each.get_days_rented() * 3
            elif each.get_movie().get_price_code() == MoviePriceCode.CHILDREN:
                this_amount += 1.5
                if each.get_days_rented() > 3:
                    this_amount += (each.get_days_rented() - 3) * 1.5

            # add frequent renter points
            frequent_renter_points += 1
            # add bonus for a two day new release rental
            if (each.get_movie().get_price_code() == MoviePriceCode.NEW_RELEASE) and each.get_days_rented() > 1:
                frequent_renter_points += 1

            # show figures for this rental
            result += "\t" + each.get_movie().get_title() + "\t" + str(this_amount) + "\n"
            total_amount += this_amount

        # add footer lines
        result += "Amount owed is " + str(total_amount) + "\n"
        result += "You earned " + str(frequent_renter_points) + " frequent renter points"

        return result

    def add_rental(self, rental: Rental):
        self._rentals.append(rental)
