import csv
import random

fruits = [
    "apple", "banana", "orange", "pear", "grape",
    "plum", "strawberry", "blueberry", "pineapple", "kiwi"
]

fruit_prices = [
    (random.choice(fruits), random.randint(1, 20)) for _ in range(30)
]

with open("fruits.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Fruit", "Price (PLN)"])  # header
    writer.writerows(fruit_prices)

print("Data has been written to fruits.csv!")
