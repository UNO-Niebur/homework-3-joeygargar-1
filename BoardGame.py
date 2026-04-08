# Homework 3 - Board Game System
# Name: Mia Garcia
# Date: 4/7/2026

def loadGameData(filename):
    
    players = {}
    events = {}
    currentTurn = ""

    with open(filename, "r") as file:
        for line in file:
            line = line.strip()

            if line == "":
                continue

            if line.startswith("Turn:"):
                currentTurn = line.split(":")[1].strip()
            else:
                parts = line.split(":")
                position = int(parts[0].strip())
                name = parts[1].strip()

                if name.startswith("Player"):
                    players[name] = position
                else:
                    events[position] = name

    return currentTurn, players, events


def saveGameData(filename, currentTurn, players, events):
    with open(filename, "w") as file:
        file.write(f"Turn: {currentTurn}\n")

        for player in players:
            file.write(f"{players[player]}: {player}\n")

        for position in events:
            file.write(f"{position}: {events[position]}\n")


def displayBoard(players, events, boardSize=30):
    print("\nBoard:")
    for space in range(1, boardSize + 1):
        contents = []

        for player in players:
            if players[player] == space:
                contents.append(player)

        if space in events:
            contents.append(events[space])

        if contents:
            print(f"{space}: " + ", ".join(contents))
        else:
            print(f"{space}: Empty")


def displayGame(currentTurn, players, events, boardSize=30):
    print("\nCurrent Game State")
    print("------------------")
    print("Current Turn:", currentTurn)

    print("\nPlayers:")
    for player in players:
        print(f"{player} is on space {players[player]}")

    print("\nEvents:")
    for position in events:
        print(f"Space {position}: {events[position]}")

    displayBoard(players, events, boardSize)


def triggerEvent(playerName, position, events):
    if position in events:
        print(f"{playerName} landed on {events[position]}!")
    else:
        print(f"{playerName} landed on an empty space.")


def switchTurn(currentTurn, players):
    playerNames = list(players.keys())
    currentIndex = playerNames.index(currentTurn)
    nextIndex = (currentIndex + 1) % len(playerNames)
    return playerNames[nextIndex]


def movePlayer(currentTurn, players, events, boardSize=30):
    print(f"\nIt is {currentTurn}'s turn.")
    spaces = int(input("How many spaces should the player move? "))

    players[currentTurn] += spaces

    if players[currentTurn] > boardSize:
        players[currentTurn] = boardSize

    print(f"{currentTurn} moved to space {players[currentTurn]}.")
    triggerEvent(currentTurn, players[currentTurn], events)


def main():
    filename = "events.txt"
    boardSize = 30

    currentTurn, players, events = loadGameData(filename)

    while True:
        displayGame(currentTurn, players, events, boardSize)

        print("\nMenu")
        print("1. Move current player")
        print("2. Switch turn")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            movePlayer(currentTurn, players, events, boardSize)
            saveGameData(filename, currentTurn, players, events)

        elif choice == "2":
            currentTurn = switchTurn(currentTurn, players)
            print("Turn switched.")
            saveGameData(filename, currentTurn, players, events)

        elif choice == "3":
            saveGameData(filename, currentTurn, players, events)
            print("Game saved. Goodbye.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()