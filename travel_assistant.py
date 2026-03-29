import pandas as pd
import pickle
import os
import random
import matplotlib.pyplot as plt
from colorama import Fore, Style, init

init(autoreset=True)

currnt_folder = os.path.dirname(__file__)

model_path = os.path.join(currnt_folder,"..","models","comfort_model.pkl")
distance_path = os.path.join(currnt_folder,"..","datasets","distances.csv")
places_path = os.path.join(currnt_folder,"..","datasets","places.csv")

with open(model_path,"rb") as f:
    model = pickle.load(f)

distance_data = pd.read_csv(distance_path)
places_data = pd.read_csv(places_path)

speed = {"Car":60,"Bus":50,"Train":80,"Flight":500}

cost = {"Car":4500,"Bus":900,"Train":1200,"Flight":6500}

while True:

    print(Fore.CYAN + "\n=== RouteWise AI Travel Assistant ===")
    print("1. Plan a trip")
    print("2. View available cities")
    print("3. Exit")

    choice = input("\nChoose an option: ")

    if choice == "3":
        print(Fore.YELLOW + "Goodbye!")
        break

    if choice == "2":

        cities = set(distance_data["from"]).union(set(distance_data["to"]))

        print(Fore.GREEN + "\nAvailable Cities:")
        for city in sorted(cities):
            print("-",city)

        continue

    if choice != "1":
        print(Fore.RED + "Invalid choice")
        continue

    start = input("\nEnter your location: ").title()
    destination = input("Enter destination: ").title()

    place_info = places_data[places_data["place"] == destination]

    if not place_info.empty:
        row = place_info.iloc[0]

        print(Fore.GREEN + "\nTravel Guide")
        print("Description:",row["description"])
        print("Best Time to Visit:",row["best_time"])
        print("Average Visit Duration:",row["visit_duration"])

    route = distance_data[
        (distance_data["from"] == start) &
        (distance_data["to"] == destination)
    ]

    if route.empty:

        print(Fore.RED + "\nRoute not available.")

        possible = distance_data[distance_data["from"] == start]["to"].tolist()

        if possible:
            print("\nAvailable destinations from",start)
            for city in possible:
                print("-",city)

        continue

    distance = route.iloc[0]["distance"]

    travel_options = []

    print(Fore.BLUE + "\nTravel Options")

    for mode in speed:

        time = round(distance/speed[mode],2)

        seat = {"Car":6,"Bus":4,"Train":8,"Flight":6}[mode]
        noise = {"Car":4,"Bus":7,"Train":3,"Flight":5}[mode]

        stability = {"Car":6,"Bus":4,"Train":8,"Flight":6}[mode]

        comfort = model.predict([[time,seat,noise,stability]])[0]

        traffic = random.choice(["Low","Medium","High"])
        road = random.choice(["Good","Moderate","Poor"])

        print(Fore.YELLOW + f"\nMode: {mode}")
        print("Travel Time:",time,"hours")
        print("Estimated Cost: ₹",cost[mode])
        print("Traffic Level:",traffic)
        print("Road Condition:",road)
        print("Comfort Level:",comfort)

        travel_options.append((mode, time, cost[mode], comfort))

    fastest = min(travel_options,key=lambda value:value[1])
    cheapest = min(travel_options,key=lambda value:value[2])

    rank={"Low":1,"Medium":2,"High":3}
    comfortable = max(travel_options,key=lambda value:rank[value[3]])

    print(Fore.CYAN + "\nRecommendations")
    print("Fastest Mode:",fastest[0])
    print("Cheapest Mode:",cheapest[0])
    print("Most Comfortable Mode:",comfortable[0])

    print(Fore.MAGENTA + "\nAI Explanation")
    print("The recommendation considers travel time, cost, and comfort predicted by the ML model.")

    score = 10 - (fastest[1]/5)

    if score < 0:
        score = 6

    print(Fore.GREEN + "\nTrip Score:",round(score,1),"/10")
    print("\nBest Time To Travel: Early morning to avoid traffic.")

    modes = [r[0] for r in travel_options]
    times = [r[1] for r in travel_options]

    plt.bar(modes,times)
    plt.title("Travel Time Comparison")
    plt.xlabel("Transport Mode")
    plt.ylabel("Time (hours)")
    plt.show()

    # use python3 code/travel_assistant.py as initial stage of the code for it to run