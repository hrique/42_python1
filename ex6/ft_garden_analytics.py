#!/usr/bin/env python3


class Plant:
    class Stats:
        def __init__(self) -> None:
            self._grow = 0
            self._age = 0
            self._show = 0

        def count_grow(self) -> None:
            self._grow += 1

        def count_age(self) -> None:
            self._age += 1

        def count_show(self) -> None:
            self._show += 1

        def display(self) -> None:
            print(f"Stats: {self._grow} grow, {self._age} age, "
                  f"{self._show} show")

    def __init__(self, name: str, height: float, age_days: int,
                 growth: float) -> None:
        self.name = name
        self._height = 0.0
        self._age_days = 0
        self._growth = 0.0
        self.set_height(height, verbose=False)
        self.set_age(age_days, verbose=False)
        self.set_growth(growth, verbose=False)
        self._stats = Plant.Stats()

    def get_stats(self) -> "Plant.Stats":
        return self._stats

    def show(self) -> None:
        self._stats.count_show()
        print(
            f"{self.name.capitalize()}: {round(self.get_height(), 1)}cm, "
            f"{self.get_age()} days old"
        )

    def get_growth(self) -> float:
        return self._growth

    def grow(self, verbose: bool = True) -> None:
        self._stats.count_grow()
        self.set_height(self.get_height() + self.get_growth(), verbose)

    def age(self, days: int = 1, verbose: bool = True) -> None:
        self._stats.count_age()
        self.set_age(self.get_age() + days, verbose)

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

    @staticmethod
    def check_age(age_days: int) -> bool:
        return age_days > 365

    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0, 0.0)


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
        self._bloomed = True


class Tree(Plant):
    class Stats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade = 0

        def count_shade(self) -> None:
            self._shade += 1

        def display(self) -> None:
            super().display()
            print(f" {self._shade} shade")

    def __init__(self, name: str, height: float, age_days: int,
                 growth: float, trunk_diameter: float) -> None:
        super().__init__(name, height, age_days, growth)
        self._trunk_diameter = 0.0
        self.set_trunk(trunk_diameter, verbose=False)
        self._stats: Tree.Stats = Tree.Stats()

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
        self._stats.count_shade()
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
        print(f" Nutritional value: {int(self._nutritional_value)}")

    def age(self, days: int = 1, verbose: bool = True) -> None:
        super().age(days, verbose)
        self._nutritional_value += 0.5

    def grow(self, verbose: bool = True) -> None:
        super().grow(verbose)
        self._nutritional_value += 0.5


class Seed(Flower):
    def __init__(self, name: str, height: float, age_days: int, growth: float,
                 color: str) -> None:
        super().__init__(name, height, age_days, growth, color)
        self._seeds = 0

    def bloom(self) -> None:
        super().bloom()
        self._seeds = 42

    def show(self) -> None:
        super().show()
        print(f" Seeds: {self._seeds}")


def display_stats(plant: Plant) -> None:
    print(f"[statistics for {plant.name.capitalize()}]")
    plant.get_stats().display()


def main() -> None:
    print("=== Garden statistics ===")
    print("=== Check year-old")
    print(f"Is 30 days more than a year? -> {Plant.check_age(30)}")
    print(f"Is 400 days more than a year? -> {Plant.check_age(400)}")
    print("\n=== Flower")
    rose = Flower("rose", 15.0, 10, 8.0, "red")
    rose.show()
    display_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow(verbose=False)
    rose.bloom()
    rose.show()
    display_stats(rose)
    print("\n=== Tree")
    oak = Tree("oak", 200.0, 365, 0.1, 5.0)
    oak.show()
    display_stats(oak)
    oak.produce_shade()
    display_stats(oak)
    print("\n=== Seed")
    sunflower = Seed("sunflower", 80.0, 45, 30.0, "yellow")
    sunflower.show()
    print("[make sunflower grow, age and bloom]")
    sunflower.grow(verbose=False)
    sunflower.age(20, verbose=False)
    sunflower.bloom()
    sunflower.show()
    display_stats(sunflower)
    print("\n=== Anonymous")
    unknown = Plant.anonymous()
    unknown.show()
    display_stats(unknown)


if __name__ == "__main__":
    main()
