from rental import Rental


class User:
    def __init__(self, username: str, password: str) -> None:
        self.__username = username
        self.__password = password
        self.__rentals = []

    def __str__(self) -> str:
        return self.__username

    def validate(self, username: str, password: str) -> bool:
        return self.__username == username and self.__password == password

    # setters and getters
    def set_username(self, username: str) -> None:
        self.__username = username

    def set_password(self, password: str) -> None:
        self.__password = password

    def set_rentals(self, rentals: list) -> None:
        self.__rentals = rentals

    def get_username(self) -> str:
        return self.__username

    def get_password(self) -> str:
        return self.__password

    def get_rentals(self) -> list:
        return self.__rentals

    def add_rentals(self, rental: Rental) -> None:
        self.__rentals.append(rental) 