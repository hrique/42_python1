#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age_days: int,
                 growth: float) -> None:
        self.name = name
        self._height = 0.0
        self._age_days = 0
        self._growth = 0.0
        self.set_height(height, verbose=False)
        self.set_age(age_days, verbose=False)
        self.set_growth(growth, verbose=False)

    def show(self) -> None:
        print(
            f"{self.name.capitalize()}: {round(self.get_height(), 1)}cm, "
            f"{self.get_age()} days old"
        )

    def get_growth(self) -> float:
        return self._growth

    def grow(self) -> None:
        self.set_height(self.get_height() + self.get_growth())

    def age(self) -> None:
        self.set_age(self._age_days + 1)

    def get_height(self) -> float:
        return self._height

    def set_height(self, new_height: float, verbose: bool = True) -> None:
        if new_height >= 0:
            self._height = new_height
            if verbose:
                print(f"Height updated: {round(self.get_height(), 1)}cm")
        else:
            print(f"{self.name.capitalize()}: Error, height can't be negative")
            print("Height update rejected")

    def get_age(self) -> int:
        return self._age_days

    def set_age(self, new_age: int, verbose: bool = True) -> None:
        if new_age >= 0:
            self._age_days = new_age
            if verbose:
                print(f"Age updated: {self.get_age()} days")
        else:
            print(f"{self.name.capitalize()}: Error, age can't be negative")
            print("Age update rejected")

    def set_growth(self, new_growth: float, verbose: bool = True) -> None:
        if new_growth >= 0:
            self._growth = new_growth
            if verbose:
                print(f"Growth updated: {round(self.get_growth(), 1)}cm")
        else:
            print(f"{self.name.capitalize()}: "
                  "Error, growth can't be negative")
            print("Growth update rejected")


def main() -> None:
    print("=== Garden Security System ===")
    rose = Plant("rose", 15.0, 10, 0.8)
    print("Plant created: ", end="")
    rose.show()
    print()
    rose.set_height(25.0)
    rose.set_age(30)
    print()
    rose.set_height(-30)
    rose.set_age(-30)
    print()
    print("Current state: ", end="")
    rose.show()


if __name__ == "__main__":
    main()
