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
    oak = Plant("oak", 200.0, 365, 0.6)
    cactus = Plant("cactus", 5.0, 90, 0.1)
    sunflower = Plant("sunflower", 80.0, 45, 0.3)
    fern = Plant("fern", 15.0, 120, 0.1)
    plants = [rose, oak, cactus, sunflower, fern]
    print("=== Plant Factory Output ===")
    for plant in plants:
        print("Created: ", end="")
        plant.show()


if __name__ == "__main__":
    main()
