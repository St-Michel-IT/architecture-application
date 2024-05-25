"""
This module aims to highlight the S.O.L.I.D. Dependency Inversion Principle.
The basic version does not follow the Dependency Inversion Principle and
therefore is to refactor.
Hint: Just adding an abstract class should do the trick.
"""


class LightBulb:
    """
    Light bulb class representing a light bulb.
    """

    def turn_on(self) -> str:
        """
        Turn on the light bulb.

            :return: A string representing the light bulb state.
        """
        return "Light bulb is on."

    def turn_off(self) -> str:
        """
        Turn off the light bulb.

            :return: A string representing the light bulb state.
        """
        return "Light bulb is off."


class PowerSwitch:
    """
    Power switch class representing a power switch.
    """

    # It works, but the PowerSwitch class is tightly coupled to the LightBulb
    # class.
    # Following the Dependency Inversion Principle should help to decouple the
    # classes.
    def __init__(self, lightbulb: LightBulb):
        """
        Constructor initializing the light bulb.
        """
        self.light_bulb = lightbulb

    def turn_on_light(self) -> str:
        """
        Turn on the light bulb.

            :return: A string representing the light bulb state.
        """
        return self.light_bulb.turn_on()

    def turn_off_light(self) -> str:
        """
        Turn off the light bulb.

            :return: A string representing the light bulb state.
        """
        return self.light_bulb.turn_off()


if __name__ == "__main__":
    hue_bulb = LightBulb()
    power_switch = PowerSwitch(hue_bulb)
    print(power_switch.turn_on_light())
    print(power_switch.turn_off_light())
