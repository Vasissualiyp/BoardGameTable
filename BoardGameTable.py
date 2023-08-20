#!/usr/bin/env python3

import subprocess
import os

# Define the games and corresponding png files
games = {
    "Dune": ["./Dune/Dune_Board.png"],
    "TicketToRide": [
        "./TicketToRideEurope/EuropeMap.png",
        "./TicketToRideEurope/USAMap.png",
    ],
    # Add more games and maps here
}

# Prompt for the game
print("Available games:")
for idx, game in enumerate(games.keys()):
    print(f"{idx + 1}. {game}")

choice = int(input("Choose the game you want to play (enter the number): ")) - 1
selected_game = list(games.keys())[choice]

# Check for multiple maps and prompt if necessary
maps = games[selected_game]
if len(maps) > 1:
    print(f"Available maps for {selected_game}:")
    for idx, map_path in enumerate(maps):
        print(f"{idx + 1}. {os.path.basename(map_path)}")

    choice = int(input("Choose the map you want to use (enter the number): ")) - 1
    selected_map = maps[choice]
else:
    selected_map = maps[0]

# Open the selected image in gwenview on the 1st desktop named "I" in bspwm
subprocess.run(["bspc", "desktop", "-f", "I"])
subprocess.run(["gwenview", selected_map])

print(f"{selected_game} is set up and ready to play!")

