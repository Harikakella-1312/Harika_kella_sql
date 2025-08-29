#Q6. Create a class Movie with attributes like title, genre, and duration.
#Create a class Showtime with movie, time, and available_seats.
#Create a class User with methods to book_ticket(showtime) and cancel_ticket(showtime).
#Use encapsulation to update seat availability and validate booking limits.
#Add exception handling for sold-out shows or invalid cancellations.

class sold_out_shows(Exception):
    pass

class invaid_cancellations(Exception):
    pass

class Movie:
    def __init__(self, title, genre, duration):
        self.__title= title
        self.__genre =genre
        self.__duration=duration
    def __str__(self):
        return f"{self.title} and {self._genre} for {self.duration}"
    
class Showtime:
    def __init__(self, movie, time, total_seats):
        self.movie = movie
        self.time = time
        self.available_seats = total_seats

    def available_seats(self):
        return self._available_seats
    
    def _update_seats(self, count):
        if count > self._available_seats:
            raise sold_out_shows(f"No enough seats available for ")
        self._available_seats -= count

    def _release_seat(self, count):
        self._available_seats += count

    def __str__(self):
        return f"{self.movie} at {self.time} and Available Seats: {self._available_seats}" 

class Users:
    def __init__(self, name):
        self.name = name
        self.booked_showtimes={}

    def book_ticket(self, showtime: Showtime, num_tickets = 1):
        if num_tickets <= 0:
            print("Invalid number of tickets")
            return
        try:
            showtime._update_seats(num_tickets)
            self.booked_showtimes[showtime] = self.booked_showtimes.get(showtime, 0) + num_tickets
            print(f"{self.name} successfully booked {num_tickets} ticket(s) for {showtime.movie.title} at {showtime.time}")
        except sold_out_shows as e:
            print("Error:", e)

        




        

