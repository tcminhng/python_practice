# Class & Object -> The way to represent data
# Class == blueprint


class HouseTemplate:
    # Constructor: describe the house
    def __init__(self, color: str, number_of_rooms: int, has_garden: bool):
        # Attributes
        self.house_color = color
        self.house_num_rooms = number_of_rooms
        self.house_has_garden = has_garden

    # Functions to describe the behaviours
    def open_door_auto(self):
        print("Door is opened")

    def close_garage(self):
        print("Garage is closed")


def main():
    # Create first house
    house1 = HouseTemplate(color="Blue", number_of_rooms=2, has_garden=False)

    # Create second house
    house2 = HouseTemplate(color="Red", number_of_rooms=2, has_garden=True)

    house1.open_door_auto()
    house2.close_garage()

    print(house2.house_color)
    print(house2.house_num_rooms)
    print(house2.house_has_garden)


if __name__ == "__main__":
    main()
