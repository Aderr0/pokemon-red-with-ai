
from os import listdir, rename
from datetime import datetime
from io import BufferedIOBase
import time
from pyboy import PyBoy, WindowEvent
from PIL import Image

from src.constants import Constants
from src.log import get_logger


class Pyboy:
    """
    Pyboy is a wrapper class for the Open Source project pyboy : https://github.com/Baekalfen/PyBoy
    This class makes it easy to load a ROM file, run the game, manipulate the screen, and send inputs
    """

    def __init__(self, sound: bool = False):
        self.logger = get_logger(__class__.__name__)

        self.sound = sound
        self.tick_count = 0

        self.game: PyBoy = self.load_rom()

    def load_rom(self) -> PyBoy:
        """Loads the ROM file.

        The ROM file location is set in the Constants class in `src/constants.py`.
        It instances a PyBoy object, thanks to the Open Source project pyboy : https://github.com/Baekalfen/PyBoy.


        Returns
        -------
        PyBoy
            The PyBoy instance with the loaded ROM
        """
        rom_path = Constants.ROM_FILE_PATH
        try:
            game = PyBoy(rom_path, sound=self.sound)
            self.logger.debug(f"Loaded ROM: {rom_path}")
            return game
        except FileNotFoundError:
            print(f"Error: ROM '{rom_path}' not found.")

    def tick(self) -> bool:
        """Increment the tick count and run the tick.

        Returns
        -------
        bool
            1 if the game is running, 0 if the game is paused
        """
        self.tick_count += 1
        return not self.game.tick()

    def screen_image(self, image_count: int | str) -> None:
        """Take a screenshot and save it to a file.

        Parameters
        ----------
        image_count : int | str
            The number of the screenshot to save
        """
        image: Image = self.game.screen_image()
        image.save(Constants.SCREENSHOTS_FILE_PATH.format(image_count=image_count))

    def save_state(self, state_file_name: BufferedIOBase) -> None:
        """Save the state of the game.

        Parameters
        ----------
        image_count : int | str
            The number of the screenshot to save
        """
        self.logger.debug(f"Saving state: {state_file_name}")
        with open(Constants.STATES_FILE_PATH.format(state_name=state_file_name), "wb") as state_file:
            self.game.save_state(state_file)

    def stop(self, save=False) -> None:
        """Close the game.

        Parameters
        ----------
        save : bool, optional
            Whether to save the game, by default False
        """
        self.game.stop(save=save)

        if save:
            try:
                new_state_file_name = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                rename(Constants.ROM_FILE_PATH + ".state", Constants.STATES_FILE_PATH.format(state_name=new_state_file_name))
            except FileNotFoundError:
                self.logger.exception(f"Error: State file {Constants.ROM_FILE_PATH + '.state'} not found.")

    def load_state(self) -> None:
        """Load a state file.

        The state file location is set in the Constants class in `src/constants.py`.
        """
        message = "\n\n\tAvailable states:"
        message += "\n0 - Start new game"

        state_files = list(filter(lambda f: f.endswith(".state"), listdir(Constants.STATES_PATH)))

        for index, file in enumerate(state_files):
            message += f"\n{index+1} - {file}"        

        self.logger.info(message)

        try:
            input_value = int(input("Choose a state: "))
        except ValueError:
            input_value = 0
        
        # New line for readability in terminal
        print("")

        if input_value > 0 and input_value <= len(state_files):
            self.logger.info(f"Loading state: {state_files[input_value-1]}")
            state_file = open(Constants.STATES_PATH + state_files[input_value-1], "rb")
            self.game.load_state(state_file)
        else:
            self.logger.info("Starting new game...")

    def show_commands(self) -> None:
        self.logger.info("\n\n\t => Commands:")
        self.logger.info("Arrow keys: Move up / down / left / right")
        self.logger.info("A: Button A on GBA")
        self.logger.info("B: Button B on GBA")
        self.logger.info("Enter: Pause on GBA")
        self.logger.info("Space: Accelerate the game")
        self.logger.info("Escape: Turn off the game")

        # New line for readability in terminal
        print("")
