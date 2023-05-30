from dataclasses import dataclass

import matplotlib.pyplot as plt
import numpy as np

CALORIE_GOAL_LIMIT = 2500
PROTEIN_GOAL = 75
FAT_GOAL = 100
CARBS_GOAL = 250

today = []

@dataclass
class Food:
    name: str
    calories: float
    protein: float
    fat: float
    carbs: float

done = False

while not done:
    print("""
    (1) Add a new food item
    (2) Visualize your progress
    (3) Quit
    """)

    choice = input("Choose an option: ")

    if choice == "1":
        print("Adding new food!")
        name = input("Name: ")
        calories = int(input("Calories: "))
        protein = int(input("Protein: "))
        fat = int(input("Fat: "))
        carbs = int(input("Carbs: "))
        food_item = Food(name, calories, protein, fat, carbs)
        today.append(food_item)
        print("Successfully added!")
    elif choice == "2":
        calorie_sum = sum(food_item.calories for food_item in today)
        protein_sum = sum(food_item.protein for food_item in today)
        fat_sum = sum(food_item.fat for food_item in today)
        carbs_sum = sum(food_item.carbs for food_item in today)

        fig, axs = plt.subplots(2, 2)
        axs[0, 0].pie([protein_sum, fat_sum, carbs_sum], labels=["Proteins", "Fats", "Carbs"], autopct="%.1f%%")
        axs[0, 0].set_title("Macros Distribution")
        axs[0, 1].bar([0, 1, 2], [protein_sum, fat_sum, carbs_sum], width=0.4)
        axs[0, 1].bar([0.5, 1.5, 2.5], [PROTEIN_GOAL, FAT_GOAL, CARBS_GOAL], width=0.4)
        axs[0, 1].set_title("Progress")
        axs[1, 0].pie([calorie_sum, CALORIE_GOAL_LIMIT - calorie_sum], labels=["Calories", "Remaining"], autopct="%.1f%%")
        axs[1, 0].set_title("Caloric Progress")
        axs[1, 1].plot(list(range(len(today))), np.cumsum([food_item.calories for food_item in today]), label="Calories Eaten")
        axs[1, 1].plot(list(range(len(today))), [CALORIE_GOAL_LIMIT] * len(today), label="Caloric Goal")
        axs[1, 1].legend()
        axs[1, 1].set_title("Caloric Goal Over Time")
        fig.tight_layout()
        plt.show()
    elif choice == "3":
        done = True
        print("Exiting the program.")
    else:
        print("Invalid choice! Please choose a valid option.")
