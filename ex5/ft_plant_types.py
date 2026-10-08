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

    def grow(self, verbose: bool = True) -> None:
        self.set_height(self.get_height() + self.get_growth(), verbose)

    def age(self, verbose: bool = True) -> None:
        self.set_age(self.get_age() + 1, verbose)

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


class Flower(Plant):
    def __init__(self, name: str, height: float, age_days: int,
                 growth: float, color: str) -> None:
        super().__init__(name, height, age_days, growth)
        self.color = color
        self._bloomed = False

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self._bloomed:
            print(f" {self.name.capitalize()} is blooming beautifully!")
        else:
            print(f" {self.name.capitalize()} has not bloomed yet")

    def bloom(self) -> None:
        print(f"[asking the {self.name} to bloom]")
        self._bloomed = True


class Tree(Plant):
    def __init__(self, name: str, height: float, age_days: int,
                 growth: float, trunk_diameter: float) -> None:
        super().__init__(name, height, age_days, growth)
        self._trunk_diameter = 0.0
        self.set_trunk(trunk_diameter, verbose=False)

    def get_trunk(self) -> float:
        return self._trunk_diameter

    def set_trunk(self, new_trunk: float, verbose: bool = True) -> None:
        if new_trunk >= 0:
            self._trunk_diameter = new_trunk
            if verbose:
                print(f"Trunk updated: {round(self.get_trunk(), 1)}cm")
        else:
            print(f"{self.name.capitalize()}: Error, trunk can't be negative")
            print("Trunk update rejected")

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {round(self.get_trunk(), 1)}cm")

    def produce_shade(self) -> None:
        print(f"[asking the {self.name} to produce shade]")
        print(
            f"Tree {self.name.capitalize()} now produces a shade of "
            f"{round(super().get_height(), 1)}cm long and "
            f"{round(self.get_trunk(), 1)}cm wide."
        )


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age_days: int, growth: float,
                 harvest_season: str) -> None:
        super().__init__(name, height, age_days, growth)
        self.harvest_season = harvest_season
        self._nutritional_value = 0.0

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season.capitalize()}")
        print(f" Nutritional value: {round(self._nutritional_value, 1)}")

    def age(self, verbose: bool = True) -> None:
        super().age(verbose)
        self._nutritional_value += 0.5

    def grow(self, verbose: bool = True) -> None:
        super().grow(verbose)
        self._nutritional_value += 0.5


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
    print()
    print("=== Vegetable")
    tomato = Vegetable("tomato", 5.0, 10, 2.1, "april")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for _ in range(20):
        tomato.grow(verbose=False)
        tomato.age(verbose=False)
    tomato.show()


if __name__ == "__main__":
    main()
