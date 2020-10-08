class Room:
    def __init__(self):
        self.description: str = ""
        self.north: int = 0
        self.east: int = 0
        self.south: int = 0
        self.west: int = 0


def print_intro():
    print("The first thing you see when you wake up is a ceiling fan slowly spinning above your head.")
    print("You don't remember your name, or why you woke up in this bed.")
    print("You have an urge to explore this unknown house.")


def main():

    print_intro()

    room_list = []

    current_room = 0

    bedroom_one = Room()
    bedroom_one.description = "You are in a small bedroom. There are doors to the north and east."
    bedroom_one.north = 4
    bedroom_one.east = 1
    bedroom_one.south = None
    bedroom_one.west = None
    room_list.append(bedroom_one)

    south_hall = Room()
    south_hall.description = "You are in the front hall of the house. The hall is north and rooms are east and west."
    south_hall.north = 5
    south_hall.east = 2
    south_hall.south = None
    south_hall.west = 0
    room_list.append(south_hall)

    garage = Room()
    garage.description = "You are in the two-car garage. There are rooms to the north and west."
    garage.north = 6
    garage.east = None
    garage.south = None
    garage.west = 1
    room_list.append(garage)

    bathroom_one = Room()
    bathroom_one.description = "You are in the ensuite of the master bedroom. There is a door to the east."
    bathroom_one.north = None
    bathroom_one.east = 4
    bathroom_one.south = None
    bathroom_one.west = None
    room_list.append(bathroom_one)

    bedroom_two = Room()
    bedroom_two.description = "You are in the master bedroom. There is a hall to the east and a door to the south."
    bedroom_two.north = None
    bedroom_two.east = 5
    bedroom_two.south = 0
    bedroom_two.west = 3
    room_list.append(bedroom_two)

    north_hall = Room()
    north_hall.description = "You are in the hallway, it continues south and there are doors to all other directions."
    north_hall.north = 8
    north_hall.east = 6
    north_hall.south = 1
    north_hall.west = 4
    room_list.append(north_hall)

    kitchen = Room()
    kitchen.description = "You are in the kitchen, something smells good. There are doors in all directions"
    kitchen.north = 9
    kitchen.east = 7
    kitchen.south = 2
    kitchen.west = 5
    room_list.append(kitchen)

    dining_room = Room()
    dining_room.description = "You are in the formal dining room. There are doors to the north and west."
    dining_room.north = 10
    dining_room.east = None
    dining_room.south = None
    dining_room.west = 6
    room_list.append(dining_room)

    porch = Room()
    porch.description = "You are in the screened-in porch. There is a room to the east and a hallway to the south."
    porch.north = None
    porch.east = 9
    porch.south = 5
    porch.west = None
    room_list.append(porch)

    living_room = Room()
    living_room.description = "You are in a spacious living room. There are doors to the east, south and west."
    living_room.north = None
    living_room.east = 10
    living_room.south = 6
    living_room.west = 8
    room_list.append(living_room)

    bathroom_two = Room()
    bathroom_two.description = "You are in the guest bathroom. There are doors to the south and west."
    bathroom_two.north = None
    bathroom_two.east = None
    bathroom_two.south = 7
    bathroom_two.west = 9
    room_list.append(bathroom_two)

    done = False
    while not done:
        print()
        print(room_list[current_room].description)
        print()
        user_choice = input("Which direction do you want to go? ")
        user_choice = user_choice.lower()

        if user_choice == "quit":
            done = True
            print()
            print("You have left the house, see you next time.")

        elif user_choice == "north" or user_choice == "n":
            next_room = room_list[current_room].north
            if next_room is None:
                print()
                print("You can't go that way.")
            else:
                current_room = next_room

        elif user_choice == "east" or user_choice == "e":
            next_room = room_list[current_room].east
            if next_room is None:
                print()
                print("You can't go that way.")
            else:
                current_room = next_room

        elif user_choice == "south" or user_choice == "s":
            next_room = room_list[current_room].south
            if next_room is None:
                print()
                print("You can't go that way.")
            else:
                current_room = next_room

        elif user_choice == "west" or user_choice == "w":
            next_room = room_list[current_room].west
            if next_room is None:
                print()
                print("You can't go that way.")
            else:
                current_room = next_room

        else:
            print("There's an error, what did you mean?")


main()
