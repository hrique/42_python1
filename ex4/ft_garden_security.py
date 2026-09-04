#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age_days, growth):
        self.name = name
        self._height = height
        self._age_days = age_days
        self._growth = growth

    def show(self):
        print(
            f"{self.name.capitalize()}: {round(self.get_height(), 1)}cm, "
            f"{self.get_age()} days old"
        )

    def get_growth(self) -> float:
        return self._growth

    def grow(self):
        self.set_height(self._height + self.get_growth())

    def age(self):
        self.set_age(self._age_days + 1)

    def get_height(self) -> float:
        return self._height

    def set_height(self, new_height):
        if new_height >= 0:
            self._height = new_height
            print(f"Height updated: {round(self.get_height())}cm")
        else:
            print(f"{self.name.capitalize()}: Error, height can't be negative")
            print("Height update rejected")

    def get_age(self) -> int:
        return self._age_days

    def set_age(self, new_age):
        if new_age >= 0:
            self._age_days = new_age
            print(f"Age updated: {self.get_age()} days")
        else:
            print(f"{self.name.capitalize()}: Error, age can't be negative")
            print("Age update rejected")


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
