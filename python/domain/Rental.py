from domain.Movie import Movie


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
