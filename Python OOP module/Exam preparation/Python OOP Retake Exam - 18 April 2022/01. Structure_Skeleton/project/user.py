class User:
    def __init__(self, username: str, age: int):
        self.username = username
        self.age = age
        self.movies_liked = []
        self.movies_owned = []

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if value == "":
            raise ValueError("Invalid username!")

        self.__username = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 6:
            raise ValueError("Users under the age of 6 are not allowed!")
        self.__age = value

    def __str__(self):
        result = f"Username: {self.__username}, Age: {self.__age}\nLiked movies:\n"
        liked_ones = "No movies liked." if len(self.movies_liked) == 0 else "\n".join([x.details() for x in self.movies_liked])
        result += liked_ones + "\n"
        result += "Owned movies:\n"
        owned_ones = "No movies owned." if len(self.movies_owned) == 0 else "\n".join([x.details() for x in self.movies_owned])
        result += owned_ones
        return result
