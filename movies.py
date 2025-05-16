class Movie:

    def __init__(self, title, year, director):
        self.title = title
        self.year = year
        self.director = director

class User:

    def __init__(self, name):
        self.name = name

class GuessGame:

    def __init__(self, movies):
        self.users = []
        self.movies = movies

    def add_user(self, user):
        self.users.append(user)

    def start_guessing(self):
        guesses = {}
        for user in self.users:
            guess = input("What year was '{}' released, {}?\n\n".format(movie1.title, user.name))
            guesses[user.name] = int(guess)

        for name, guess in guesses.items():
            if guess == movie1.year:
                print("You guessed the year of the movie {}.".format(name))
            else:
                print("Sorry, you were wrong {}.".format(name))






movie1 = Movie("The Godfather", 1972, "Coppola")
#movie2 = Movies("Paths of Glory", 1957, "Kubrick")

user1 = User("Daniel")
user2 = User("Mila")

game = GuessGame([movie1])
game.add_user(user1)
game.add_user(user2)
game.start_guessing()
