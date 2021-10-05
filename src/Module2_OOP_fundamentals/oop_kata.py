CREW_IMMERSION_MULTIPLIER = 1.5


class Ship:
    """
    This class describes an instance of a simple ship, its immersion and crew size.
    """
    crew_immersion_multiplier = CREW_IMMERSION_MULTIPLIER

    def __init__(self, immersion, crew):
        self.immersion = immersion
        self.crew = crew

    def is_worth_it(self):
        """
        The method for estimation the class instance.
        (to decide if the ship is worthy to loot)

        Every ship that has a immersion of more than 20 units without crew is considered worthy to loot.
        Taking into account that an average crew member on board adds 1.5 units to the immersion.

        :return: bool
        """
        return True if self.immersion - self.crew * Ship.crew_immersion_multiplier > 20 else False

    def __str__(self):
        """
        Simple (user-friendly) str representation of the instance

        :return: str
        """
        return f"Crew: {self.crew} members. Immersion: {self.immersion} units."


fruit = Ship(15, 10)   # False
wood = Ship(20, 10)    # False
silver = Ship(36, 10)  # True
gold = Ship(50, 10)    # True

fleet_lst = [fruit, wood, silver, gold]
for ship in fleet_lst:
    print(ship, ship.is_worth_it())
