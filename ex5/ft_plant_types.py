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


class Flower(Plant):
    def __init__(self, name, height, age_days, growth, color):
        super().__init__(name, height, age_days, growth)
        self.color = color
        self._bloomed = False

    def show(self):
        super().show()
        print(f" Color: {self.color}")
        if self._bloomed:
            print(f" {self.name.capitalize()} is blooming beautifully!")
        else:
            print(f" {self.name.capitalize()} has not bloomed yet")

    def bloom(self):
        print(f"[asking the {self.name} to bloom]")
        self._bloomed = True


class Tree(Plant):
    def __init__(self, name, height, age_days, growth, trunk_diametter):
        super().__init__(name, height, age_days, growth)
        self._trunk_diametter = trunk_diametter

    def get_trunk(self) -> float:
        return self._trunk_diametter

    def show(self):
        super().show()
        print(f" Trunk diameter: {round(self.get_trunk(), 1)}cm")

    def produce_shade(self):
        print(f"[asking the {self.name} to produce shade]")
        print(
            f"Tree {self.name.capitalize()} now produces a shade of "
            f"{round(super().get_height(), 1)}cm long and "
            f"{round(self.get_trunk(), 1)}cm wide."
        )


class Vegetable(Plant):
    def __init__(self, name, height, age_days, growth, harvest_season,
                nutritional_value):
        super().__init__(name, height, age_days, growth)
        self.harvest_season = harvest_season
        self._nutritional_value = nutritional_value


def main() -> None:
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose = Flower("rose", 15.0, 10, 0.8, "red")
    rose.show()
    rose.bloom()
    rose.show()
    print()
    print("=== Tree")
    oak = Tree("oak", 200.0, 365, 0.1, 5.0)
    oak.show()
    oak.produce_shade()



if __name__ == "__main__":
    main()
