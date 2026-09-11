#!/usr/bin/env python3


class Plant:
    class Stats:
        def __init__(self):
            self._grow_count = 0
            self._age_count = 0
            self._show_count = 0

    def __init__(self, name: str, height: float, age_days: int,
                 growth: float) -> None:
        self.name = name
        self._height = height
        self._age_days = age_days
        self._growth = growth
        self._stats = Plant.Stats()

    def show(self) -> None:
        print(
            f"{self.name.capitalize()}: {round(self.get_height(), 1)}cm, "
            f"{self.get_age()} days old"
        )

    def get_growth(self) -> float:
        return self._growth

    def grow(self, verbose: bool = True) -> None:
        self.set_height(self._height + self.get_growth(), verbose)

    def age(self, verbose: bool = True) -> None:
        self.set_age(self._age_days + 1, verbose)

    def get_height(self) -> float:
        return self._height

    def set_height(self, new_height: float, verbose: bool = True) -> None:
        if new_height >= 0:
            self._height = new_height
            if verbose:
                print(f"Height updated: {round(self.get_height())}cm")
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

    @staticmethod
    def check_age(given_age: int) -> bool:
        if given_age > 365:
            return True
        else:
            return False

    @classmethod
    def anonymous_plant(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0, 0)


class Flower(Plant):
    class Stats(Plant.Stats):
        def __init__(self):
            super().__init__()

    def __init__(self, name: str, height: float, age_days: int, growth: float,
                 color: str) -> None:
        super().__init__(name, height, age_days, growth)
        self.color = color
        self._bloomed = False
        self._stats = Flower.Stats()

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self._bloomed:
            print(f" {self.name.capitalize()} is blooming beautifully!")
        else:
            print(f" {self.name.capitalize()} has not bloomed yet")

    def bloom(self, verbose: bool = True) -> None:
        self._bloomed = True
        if verbose:
            print(f"[asking the {self.name} to bloom]")


class Tree(Plant):
    class Stats(Plant.Stats):
        def __init__(self):
            super().__init__()
            self._shade_count = 0

    def __init__(self, name: str, height: float, age_days: int, growth: float,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age_days, growth)
        self._trunk_diameter = trunk_diameter
        self._stats = Tree.Stats()

    def get_trunk(self) -> float:
        return self._trunk_diameter

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
        class Stats(Plant.Stats):
        def __init__(self):
            super().__init__()
    def __init__(self, name: str, height: float, age_days: int, growth: float,
                 harvest_season: str, nutritional_value: int) -> None:
        super().__init__(name, height, age_days, growth)
        self.harvest_season = harvest_season
        self._nutritional_value = nutritional_value

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harvest_season.capitalize()}")
        print(f" Nutritional value: {round(self._nutritional_value)}")

    def age_and_grow(self, days: int) -> None:
        print(f"[make tomato grow and age for {days} days]")
        for _ in range(days):
            self.grow(verbose=False)
            self.age(verbose=False)
            self._nutritional_value += 1


class Seed(Flower):
    def __init__(self, name: str, height: float, age_days: int, growth: float,
                 color: str, seeds: int) -> None:
        super().__init__(name, height, age_days, growth, color)
        self._seeds = seeds
    
    def show(self) -> None:
        super().show()
        print(f" Seeds: {self._seeds}")

    def bloom(self) -> None:
        print(f"[make {self.name} grow, age and bloom]")
        super().bloom(verbose=False)
        for _ in range(20):
            self.grow(verbose=False)
            self.age(verbose=False)
        self._seeds += 42


def main() -> None:
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.check_age(30)}")
    print(f"Is 400 days more than a year? -> {Plant.check_age(400)}")
    print()
    print("=== Flower")
    rose = Flower("rose", 15.0, 10, 1.5, "red")
    rose.show()
    print()
    print("=== Tree")
    oak = Tree("oak", 200.0, 365, 1.9, 5.0)
    oak.show()
    print()
    print("=== Seed")
    sunflower = Seed("sunflower", 80.0, 45, 1.5, "yellow", 0)
    sunflower.show()
    sunflower.bloom()
    sunflower.show()
    print()
    print("=== Anonymous")
    unknown = Plant.anonymous_plant()
    unknown.show()


if __name__ == "__main__":
    main()
