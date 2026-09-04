#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        print(
            f"{self.name.capitalize()}: {self.height}cm, {self.age} days old"
        )


def main() -> None:
    print("=== Garden Plant Registry ===")
    rose = Plant("rose", 25, 30)
    rose.show()
    sunflower = Plant("sunflower", 80, 45)
    sunflower.show()
    cactus = Plant("cactus", 15, 120)
    cactus.show()


if __name__ == "__main__":
    main()
