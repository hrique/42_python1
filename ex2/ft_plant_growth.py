#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age_days, growth):
        self.name = name
        self.height = height
        self.age_days = age_days
        self.growth = growth

    def show(self):
        print(
            f"{self.name.capitalize()}: {round(self.height, 1)}cm, "
            f"{self.age_days} days old"
        )

    def grow(self):
        self.height += self.growth

    def age(self):
        self.age_days += 1


def main() -> None:
    rose = Plant("rose", 25.0, 30, 0.8)
    print("=== Garden Plant Growth ===")
    rose.show()
    start_height = rose.height
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        rose.grow()
        rose.age()
        rose.show()
    print(f"Growth this week: {round(rose.height - start_height, 1)}cm")


if __name__ == "__main__":
    main()
