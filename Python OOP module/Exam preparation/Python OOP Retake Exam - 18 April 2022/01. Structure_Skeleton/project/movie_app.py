from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def register_user(self, username: str, age: int):
        if username not in [x.username for x in self.users_collection]:
            user = User(username, age)
            self.users_collection.append(user)
            return f"{username} registered successfully."

        raise Exception("User already exists!")

    def upload_movie(self, username: str, movie: Movie):
        if username not in [x.username for x in self.users_collection]:
            raise Exception("This user does not exist!")
        user = next(filter(lambda u: u.username == username, self.users_collection))
        if movie.owner.username != username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        if movie in self.movies_collection:
            raise Exception(f"Movie already added to the collection!")

        self.movies_collection.append(movie)
        user.movies_owned.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        if movie.owner.username != username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        for key, value in kwargs.items():
            if key == "title":
                movie.title = value
            elif key == "year":
                movie.year = value
            elif key == "age_restriction":
                movie.age_restriction = value

        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        if movie.owner.username != username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        self.movies_collection.remove(movie)
        user = next(filter(lambda u: u.username == username, self.users_collection))
        user.movies_owned.remove(movie)
        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        user = next(filter(lambda u: u.username == username, self.users_collection))
        if movie.owner.username == username:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")
        if movie in user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")
        movie.likes += 1
        user.movies_liked.append(movie)
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        user = next(filter(lambda u: u.username == username, self.users_collection))
        if movie not in user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        movie.likes -= 1
        user.movies_liked.remove(movie)
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        if not self.movies_collection:
            return f"No movies found."
        new_collection = sorted(self.movies_collection, key=lambda x: (-x.year, x.title))
        result = [x.details() for x in new_collection]
        return "\n".join(result)

    def __str__(self):
        result = ["All users: "]
        users = "No users." if not self.users_collection else ", ".join([x.username for x in self.users_collection])
        result[0] += users
        result.append("All movies: ")
        movies = "No movies." if not self.movies_collection else ", ".join([x.title for x in self.movies_collection])
        result[1] += movies
        return "\n".join(result)
