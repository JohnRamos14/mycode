#!/usr/bin/python3
"""Looping with for challenge"""

def main():
    """runtime"""

    farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

    # animals from NE Farm
    NE_animals = farms[0]["agriculture"]

    # for loop to return all the animals from the NE Farm
    for ne in NE_animals:
        print(ne)

    # loop through farms to get farm names
    for farm in farms:
        print("\n", farm["name"])

    farm_name = input("\nWhich farm would you like to know more about?\n ")

    # loop to display plants/animals that are raised on the farm selected by user
    for farm in farms:
        if farm["name"].lower() ==  farm_name.lower():
            print(farm["agriculture"])


if __name__ == "__main__":
    main()
